from copy import deepcopy
from dataclasses import asdict
from functools import partial
from itertools import product
from logging import getLogger
from multiprocessing import Pool, cpu_count
from sys import stderr
from typing import Tuple

import numpy as np
import scipy.sparse as sp
import torch
from jaxtyping import Bool, Float, Int
from scipy.special import logsumexp
from tqdm import tqdm

from cp4bal.dataset import CSBM, ActiveLearningDataset

from .base import Model
from .cache import Cache
from .configs import BayesianLikelihoodConfig, BayesOptimalConfig
from .enums import ApproximationType, BayesianPrediction
from .prediction import Prediction

logger = getLogger(__name__)


class BayesOptimalModel(Model):
    def __init__(self, config: BayesOptimalConfig, dataset: ActiveLearningDataset):
        if not isinstance(dataset.base, CSBM):
            raise ValueError("BayesOptimalModel requires CSBMDataset as it uses generative distribution")
        super().__init__(config=config, dataset=dataset)
        self.approximation_type = config.approximation_type
        self.batch_size = config.batch_size
        self.num_samples = config.num_samples
        self.prediction = config.prediction
        self.graph = dataset.base
        self.importance_prob = config.importance_prob
        self.normalized = config.normalized
        self.prediction_cache = Cache[Prediction]()
        self.mask_labeled_cache = Cache[Bool[np.ndarray, " num_nodes"]]()
        self.confidence_likelihood_config = BayesianLikelihoodConfig(**asdict(config.confidence_likelihood))
        self.prediction_likelihood_config = BayesianLikelihoodConfig(**asdict(config.prediction_likelihood))

        # beam serch parameters
        self.beam_width = config.beam_width
        self.beam_search_num_iterations = config.beam_search_num_iterations

        # variational inference parameters
        self.vi_max_iterations = config.vi_max_iterations
        self.vi_convergence_tolerance = config.vi_convergence_tolerance

        # flags
        self.predict_train = (
            config.predict_train
        )  # if set, predicts with 100% confidence the true label for train nodes
        self.use_cache = config.cached
        self.multiprocessing = True
        self.verbose = True  # for debugging

    def reset_parameters(self):
        self._reset_all_caches()
        return super().reset_parameters()

    def _reset_all_caches(self):
        self.prediction_cache.reset()
        self.mask_labeled_cache.reset()

    def _update_prediction_cache(self, prediction: Prediction):
        if self.use_cache:
            self.prediction_cache.update(prediction)

    def _update_mask_labeled_cache(self, mask_labeled: Bool[np.ndarray, " num_nodes"]):
        if self.use_cache:
            self.mask_labeled_cache.update(mask_labeled)

    def _get_cached_prediction_if_mask_matches(self, mask_labeled: Bool[np.ndarray, " num_nodes"]) -> Prediction | None:
        cached_mask = self.mask_labeled_cache.get()
        if not self.use_cache or cached_mask is None:
            return None
        if (cached_mask == mask_labeled).all():
            logger.info("mask matches, returning cached prediction")
            return self.prediction_cache.get()
        return None

    def _compute_total_confidence(
        self,
        mask_fixed: Bool[np.ndarray, " num_nodes"],
        x: Float[np.ndarray, "num_nodes feature_dim"],
        y: Int[np.ndarray, " num_nodes"],
        likelihood_config: BayesianLikelihoodConfig,
    ) -> Float[np.ndarray, "num_nodes num_classes"]:
        match self.approximation_type:
            case ApproximationType.VARIATIONAL_INFERENCE:
                history = self._marginal_class_labels_variational_inference(
                    mask_fixed=mask_fixed,
                    x=x,
                    y=y,
                    likelihood_config=likelihood_config,
                    initial_confidence=None,
                    return_history=True,
                )
                return history[-1]
            case _:
                raise NotImplementedError(f"method {self.approximation_type} is not implemented")

    def _compute_aleatoric_confidence(
        self,
        x: Float[np.ndarray, "num_nodes feature_dim"],
        y: Int[np.ndarray, " num_nodes"],
        likelihood_config: BayesianLikelihoodConfig,
    ) -> Float[np.ndarray, "num_nodes num_classes"]:
        """compute the aleatoric confidence of the model. requires heavy computation: [C]^|U|

        Args:
            x (Float[np.ndarray, "num_nodes feature_dim"]): Node features
            y (Int[np.ndarray, " num_nodes"]): Node labels
            likelihood_config (BayesianLikelihoodConfig): Configuration for computing the likelihood

        Returns:
            Float[np.ndarray, "num_nodes num_classes"]: Aleatoric confidence
        """
        log_likelihood = np.zeros((self.graph.num_nodes, self.graph.num_classes))
        iterator = tqdm(
            list(product(range(self.graph.num_nodes), range(self.graph.num_classes))),
            desc="Alea",
            disable=not self.verbose,
        )
        for i, c in iterator:
            y_ic = y.copy()
            y_ic[i] = c
            log_likelihood[i, c] = self.graph.conditional_log_likelihood(
                y=y_ic[None, :],
                x=x[None, :],
                use_adjacency=likelihood_config.use_adjacency,
                use_features=likelihood_config.use_features,
                use_non_edges=likelihood_config.use_non_edges,
            )
        return log_likelihood

    def predict(self, batch, acquisition: bool = False) -> Prediction:
        _ = acquisition  # acquisition is not used in this model
        x = batch.x.numpy()
        y = batch.y.numpy()
        mask_labeled = batch.mask_train_l.numpy()

        prediction = self._get_cached_prediction_if_mask_matches(mask_labeled)
        if prediction is not None:
            return prediction

        total_confidence = self._compute_total_confidence(
            mask_fixed=mask_labeled, x=x, y=y, likelihood_config=self.confidence_likelihood_config
        )
        aleatoric_confidence = self._compute_aleatoric_confidence(
            x=x, y=y, likelihood_config=self.confidence_likelihood_config
        )

        match self.prediction:
            case BayesianPrediction.MARGINAL:
                probabilities = torch.from_numpy(self._probability_from_loglikelihood(total_confidence))
            case BayesianPrediction.JOINT:  # NOTE: heavy computation
                predicted_assignment = self._maximum_likelihood_assignment(
                    mask_fixed=mask_labeled, x=x, y=y, likelihood_config=self.prediction_likelihood_config
                )
                probabilities = np.zeros((self.graph.num_nodes, self.graph.num_classes), dtype=float)
                probabilities[np.arange(probabilities.shape[0]), predicted_assignment] = 1.0
                probabilities = torch.from_numpy(probabilities)
            case BayesianPrediction.JOINT_BEAM_SEARCH:
                maximum_likelihood_assignments, log_likelihoods = self._beam_search(
                    mask_fixed=mask_labeled,
                    x=x,
                    y=y,
                    likelihood_config=self.prediction_likelihood_config,
                    rg=np.random.default_rng(),
                )
                predicted_assignment = maximum_likelihood_assignments[log_likelihoods.argmax()]
                probabilities = np.zeros((self.graph.num_nodes, self.graph.num_classes), dtype=float)
                probabilities[np.arange(probabilities.shape[0]), predicted_assignment] = 1.0
                probabilities = torch.from_numpy(probabilities)
            case (
                BayesianPrediction.JOINT_CACHED_BEAM_SEARCH,
                BayesianPrediction.JOINT_CACHED_LIKELIHOOD,
            ):
                raise NotImplementedError
            case _:
                raise ValueError(f"Unknown prediction type: {self.prediction}")

        if self.predict_train:  # Predict 1.0 for the labeled nodes at the labeled class
            labeled_indices = list(np.where(mask_labeled)[0])
            probabilities[labeled_indices] = 0.0
            probabilities[labeled_indices, batch.y[labeled_indices]] = 1.0

        prediction = Prediction(
            probabilities=probabilities[None, ...],
            total_confidence=torch.from_numpy(total_confidence),
            aleatoric_confidence=torch.from_numpy(aleatoric_confidence),
        )

        if self.use_cache:
            self._update_prediction_cache(prediction)
            self._update_mask_labeled_cache(mask_labeled)

        return prediction

    @staticmethod
    def _probability_from_loglikelihood(
        log_likelihood: Float[np.ndarray, "num_nodes num_classes"],
    ) -> Float[np.ndarray, "num_nodes num_classes"]:
        """Convert log-likelihood to probabilities using logsumexp."""
        return np.exp(log_likelihood - logsumexp(log_likelihood, axis=-1, keepdims=True))

    def _maximum_likelihood_assignment(
        self,
        mask_fixed: Bool[np.ndarray, " num_nodes"],
        x: Float[np.ndarray, "num_nodes feature_dim"],
        y: Int[np.ndarray, " num_nodes"],
        likelihood_config: BayesianLikelihoodConfig,
    ) -> Int[np.ndarray, " num_nodes"]:
        """Computes the maxmimum likelihood estimate for p(y_u | y_o, X, A) jointly.

        Args:
            mask_fixed (Bool[np.ndarray, 'num_nodes']): observed nodes
            x (Float[np.ndarray, 'num_nodes feature_dim']): node features
            y (Int[np.ndarray, 'num_nodes']): node labels (valid only where `mask_fixed` is true)
            likelihood_config (BayesianLikelihoodConfig): configuration for computing the likelihood

        Returns:
            Int[np.ndarray, 'num_nodes']: the assignment that maximizes the likelihood
        """
        num_assignments = int(self.graph.num_classes ** (~mask_fixed).sum())
        if self.verbose:
            logger.info(f"Joint assignment: Testing {num_assignments} assignments")
        if self.multiprocessing:
            # distribute all assignments to the number of workers
            num_assignments_per_workers = max(1, num_assignments // cpu_count())
            iterator = [
                (start, min(num_assignments_per_workers, num_assignments - start))
                for start in range(0, num_assignments, num_assignments_per_workers)
            ]
            job = partial(
                compute_argmax_joint_likelihood_job,
                y=y.copy(),
                mask_fixed=mask_fixed.copy(),
                x=x.copy(),
                classifier=deepcopy(self),
                likelihood_config=likelihood_config,
            )
            if self.verbose:
                with Pool(processes=cpu_count()) as pool:
                    results = list(
                        tqdm(
                            pool.starmap(job, iterator),
                            total=len(iterator),
                            desc="Processing assignments",
                            file=stderr,
                        )
                    )
            else:
                with Pool(processes=cpu_count()) as pool:
                    results = pool.starmap(job, iterator)
            log_likelihoods, assignments = zip(*results)
            assignment = assignments[np.array(log_likelihoods).argmax()]
        else:
            _, assignment = compute_argmax_joint_likelihood_job(
                0,
                num_assignments,
                y=y.copy(),
                mask_fixed=mask_fixed.copy(),
                x=x.copy(),
                classifier=deepcopy(self),
                likelihood_config=likelihood_config,
                progress_bar=self.verbose,
            )
        return assignment

    def _beam_search(
        self,
        mask_fixed: Bool[np.ndarray, " num_nodes"],
        x: Float[np.ndarray, "num_nodes feature_dim"],
        y: Int[np.ndarray, " num_nodes"],
        likelihood_config: BayesianLikelihoodConfig,
        rg: np.random.Generator,
    ) -> Tuple[Int[np.ndarray, " num_nodes"], Float[np.ndarray, " num_nodes"]]:
        """Estimate the maximum likelihood assignment using beam search. (Modified from the original code)

        Args:
            mask_fixed (Bool[np.ndarray, 'num_nodes']): fixed nodes (observed)
            x (Bool[np.ndarray, 'num_nodes feature_dim']): node features
            y (Int[np.ndarray, 'num_nodes']): node labels (valid only where `mask_fixed` is true)
            likelihood_config (BayesianLikelihoodConfig): configuration for computing the likelihood
            rg (np.random.Generator): random number generator for reproducibility

        Returns:
            Int[np.ndarray, 'num_nodes']: the best label assignment of the beam for unobserved nodes
            Float[np.ndarray, 'num_nodes']: the conditional log likelihood of the assignment
        """
        indices_not_fixed = np.where(~mask_fixed)[0]
        num_classes = self.graph.num_classes
        num_unlabeled_nodes = indices_not_fixed.shape[0]

        beam = np.tile(y, (self.beam_width, 1))  # shape: (beam_width, num_nodes)
        # initialize beam with random labels for unlabeled nodes
        beam[:, ~mask_fixed] = rg.integers(low=0, high=num_classes, size=(self.beam_width, num_unlabeled_nodes))

        for _ in tqdm(range(self.beam_search_num_iterations), desc="beam search", disable=not self.verbose):
            for idx in range(num_unlabeled_nodes):
                beam: Int[np.ndarray, "beam_width * num_classes num_nodes"] = np.tile(
                    beam, (num_classes, 1)
                )  # shape: (beam_width * num_classes, num_nodes)
                node_idx = indices_not_fixed[idx]
                # update beam[:, node_idx] with all possible classes `c`
                for c in range(num_classes):
                    # set the class for the current node in the beam
                    start = c * self.beam_width
                    end = start + self.beam_width
                    beam[start:end, node_idx] = c
                beam = np.unique(beam, axis=0)
                log_likelihoods = self.graph.conditional_log_likelihood(
                    y=beam,
                    x=x[None, :],
                    use_adjacency=likelihood_config.use_adjacency,
                    use_features=likelihood_config.use_features,
                    use_non_edges=likelihood_config.use_non_edges,
                )
                # Keep only the top-`beam_width` beams
                best_beam_indices = np.argpartition(log_likelihoods, -self.beam_width)[-self.beam_width :]
                beam: Int[np.ndarray, "beam_width num_nodes"] = beam[best_beam_indices]
                log_likelihoods = log_likelihoods[best_beam_indices]

        return beam, log_likelihoods

    def _marginal_class_labels_variational_inference(
        self,
        mask_fixed: Bool[np.ndarray, " num_nodes"],
        x: Float[np.ndarray, "num_nodes feature_dim"],
        y: Int[np.ndarray, " num_nodes"],
        likelihood_config: BayesianLikelihoodConfig,
        initial_confidence: Float[np.ndarray, "num_nodes num_classes"] | None = None,
        return_history: bool = False,
    ):
        edge_indices = self.graph.edge_indices.numpy()
        A = sp.coo_matrix(
            (np.ones(edge_indices.shape[1]), edge_indices),
            shape=(self.graph.num_nodes, self.graph.num_nodes),
        ).tocsr()
        A = np.array(A.todense())  # Materialize the non-edges as well, since we have to sum over them as well

        # log_probability_features[u, c] = p(X_u | y_u=c)
        log_probability_features = self.graph._feature_log_likelihood(x)

        # log_probability_adjacency[u, c1, v, c2] = p(A_uv | y_u=c1, y_v=c2)
        log_probability_adjacency = (A > 0)[:, None, :, None] * np.log(self.graph.affiliation_matrix[None, :, None, :])

        if likelihood_config.use_non_edges:
            log_probability_adjacency += (np.isclose(A, 0))[:, None, :, None] * np.log(
                1 - self.graph.affiliation_matrix[None, :, None, :]
            )
        log_probability_adjacency[np.arange(self.graph.num_nodes), :, np.arange(self.graph.num_nodes), :] = (
            0  # We do not model self-loops
        )

        if initial_confidence is None:
            confidence = np.random.uniform(
                0, 1, size=(self.graph.num_nodes, self.graph.num_classes)
            )  # np.ones((self.graph.num_nodes, self.graph.num_classes))
            confidence /= confidence.sum(1, keepdims=True)
        else:
            confidence = initial_confidence.copy()

        confidence[mask_fixed] = 0.0
        confidence[np.where(mask_fixed), y[mask_fixed]] = 1.0

        history = [confidence]

        log_prior = np.log(self.graph.class_prior.numpy())
        iterator = tqdm(range(self.vi_max_iterations), desc="EM step", disable=not self.verbose)
        for iteration in iterator:
            # The confidence (probability distribution) for fixed nodes will also be fixed

            # Update the confidence for other nodes
            log_confidence_new = np.zeros_like(confidence)
            log_confidence_new += log_prior[None, :]
            if likelihood_config.use_adjacency:
                log_confidence_new += (log_probability_adjacency * confidence[None, None, ...]).sum(axis=(-1, -2))
            if likelihood_config.use_features:
                log_confidence_new += log_probability_features
            confidence_new = np.exp(log_confidence_new - logsumexp(log_confidence_new, axis=1, keepdims=True))
            confidence_new[mask_fixed] = 0.0
            confidence_new[np.where(mask_fixed), y[mask_fixed]] = 1.0
            residual = np.abs(confidence - confidence_new)[~mask_fixed]
            confidence = confidence_new

            if return_history:
                history.append(confidence)
            else:
                history = [confidence]

            if (residual < self.vi_convergence_tolerance).all():
                logger.info(f"Converged after {iteration + 1} iteration(s).")
                break
            else:
                iterator.set_description(f"Average residual {residual.mean():.5f}, Max residual {residual.max():.5f}")
        return np.stack(history)


def compute_argmax_joint_likelihood_job(
    start: int,
    num: int,
    classifier: BayesOptimalModel,
    mask_fixed: Bool[np.ndarray, " num_nodes"],
    x: Float[np.ndarray, "num_nodes feature_dim"],
    y: Int[np.ndarray, " num_nodes"],
    likelihood_config: BayesianLikelihoodConfig,
    progress_bar: bool = True,
) -> Tuple[float, Int[np.ndarray, " num_nodes"]]:
    """Computes maximum over joint likelihoods for different assignments y to the non-fixed nodes.
    This function requires heavy computation

    Args:
        start (int): at which assignment to start
        num (int): how many assignments to try
        classifier (BayesOptimal): the classifier
        mask_fixed (Bool[np.ndarray, 'num_nodes']): which nodes in y are fixed
        x (Float[np.ndarray, "num_nodes feature_dim"]): features
        y (Int[np.ndarray, 'num_nodes']): labels (only relevant for where `mask_fixed` is true)
        likelihood_config (BayesianLikelihoodConfig): configuration for computing the likelihood
        progress_bar (bool): Whether to print a progress bar

    Returns:
        log_likelihood_best (float): the maximal log likelihood computed in this job
        y_best (Int[np.ndarray, 'num_nodes']): assignment that corresponds to this log likelihood
    """
    num_classes = classifier.graph.num_classes

    max_log_likelihood, best_assignment = -np.inf, None
    iterator = range(start, start + num, classifier.batch_size)
    if progress_bar:
        iterator = tqdm(
            iterator,
            desc="Sequentially computing argmax over joint likelihoods",
            file=stderr,
        )

    for start_idx in iterator:
        end_idx = min(start_idx + classifier.batch_size, start + num)

        # generate assignments by transforming indices into base `num_classes`
        assignments = np.repeat(y[None, :], end_idx - start_idx, axis=0)
        assignment = np.arange(start_idx, end_idx, 1)  # "running" assignment in base
        for node_idx in np.where(~mask_fixed)[0]:
            assignments[:, node_idx] = assignment % num_classes
            assignment //= num_classes

        log_likelihoods_batch = classifier.graph.conditional_log_likelihood(
            y=assignments,
            x=x[None, :],
            use_adjacency=likelihood_config.use_adjacency,
            use_features=likelihood_config.use_features,
            use_non_edges=likelihood_config.use_non_edges,
        )
        max_log_likelihood_batch_idx = log_likelihoods_batch.argmax()
        max_log_likelihood_batch = log_likelihoods_batch[max_log_likelihood_batch_idx]
        if max_log_likelihood_batch > max_log_likelihood:
            max_log_likelihood, best_assignment = (
                max_log_likelihood_batch,
                assignments[max_log_likelihood_batch_idx],
            )

    return max_log_likelihood, best_assignment
