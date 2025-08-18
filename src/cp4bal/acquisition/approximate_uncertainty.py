from itertools import product
from logging import getLogger

import numpy as np
import scipy.special
import torch
from jaxtyping import Bool, Float, Int
from sklearn.linear_model import LogisticRegression
from torch import Tensor
from tqdm import tqdm

from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import CSBM, ActiveLearningDataset, GraphData
from cp4bal.dataset.enums import DatasetSplit
from cp4bal.model import Model, ModelFactory
from cp4bal.model.configs import ModelConfig
from cp4bal.model.sgc import SGC

from .base import Acquisition
from .configs import ApproximateUncertaintyAcquisitionConfig

logger = getLogger(__name__)


class ApproximateUncertaintyAcquisition(Acquisition):
    def __init__(self, config: ApproximateUncertaintyAcquisitionConfig):
        super().__init__(config=config)
        self.confidence_propagation = config.confidence_propagation
        self.uncertainty_type = config.uncertainty_type
        self.aleatoric_confidence_with_left_out_node = config.aleatoric_confidence_with_left_out_node
        self.aleatoric_confidence_labels_num_samples = config.aleatoric_confidence_labels_num_samples
        self.compute_as_ratio = config.compute_as_ratio
        self.verbose = True

    @torch.no_grad()
    def select(
        self,
        model: Model,
        dataset: ActiveLearningDataset,
        budget: int,
        generator: torch.Generator,
    ) -> list[int]:
        _ = generator

        mask_train_u = dataset.data.mask_train_u.clone()
        mask_train_l = dataset.data.mask_train_l.clone()

        with torch.no_grad():
            prediction = model.predict(dataset.data, acquisition=True)

        total_confidence = prediction.get_probabilities()
        total_confidence = total_confidence.mean(dim=0)

        mask_predict_nodes = np.ones(dataset.num_nodes, dtype=bool)
        mask_predict_nodes &= dataset.data.get_mask(DatasetSplit.TRAIN_ALL).cpu().numpy()

        if self.compute_as_ratio:
            epistemic_uncertainty = self.epistemic_uncertainty_mp(
                mask_predict=torch.tensor(mask_predict_nodes),
                mask_train=mask_train_l,
                total_confidence=total_confidence,
                model=model,
                dataset=dataset,
                model_config=model.config,
                features_only=False,
            )
        else:
            assert isinstance(model, SGC)
            epistemic_uncertainty = self.epistemic_uncertainty_esp(
                mask_predict=torch.from_numpy(mask_predict_nodes),
                mask_train=mask_train_l,
                total_confidence=total_confidence,
                model=model,
                batch=dataset.data,
                features_only=False,
            )

        if self.confidence_propagation:
            acquired_indices = []
            mask_train_Q = torch.zeros_like(mask_train_l, dtype=torch.bool)
            for _ in range(budget):
                values_for_acquisition = epistemic_uncertainty - self._calculate_confidence_propagation(
                    mask_train_u=mask_train_u,
                    mask_train_Q=mask_train_Q,
                    dataset=dataset,
                )
                indices_train_u = torch.where(mask_train_u)[0]
                possible_values_for_acquisition = values_for_acquisition[mask_train_u]
                acquired_index = indices_train_u[np.argsort(-possible_values_for_acquisition)[0]]
                mask_train_Q[acquired_index] = True
                mask_train_u[acquired_index] = False
                acquired_indices.append(acquired_index.item())
        else:
            values_for_acquisition = epistemic_uncertainty
            indices_train_u = torch.where(mask_train_u)[0]
            possible_values_for_acquisition = values_for_acquisition[mask_train_u]
            acquired_indices = indices_train_u[np.argsort(-possible_values_for_acquisition)[:budget]].tolist()
            mask_train_l[acquired_indices] = True
            mask_train_u[acquired_indices] = False

        return acquired_indices

    def _calculate_confidence_propagation(
        self,
        mask_train_u: Bool[Tensor, " n"],
        mask_train_Q: Bool[Tensor, " n"],
        dataset: ActiveLearningDataset,
    ) -> Float[Tensor, " n"]:
        if not isinstance(dataset.base, CSBM):
            raise ValueError("Confidence propagation is only implemented for CSBM datasets")

        if mask_train_Q.sum() == 0:
            # no propagation for empty Q
            return torch.zeros_like(mask_train_u, dtype=torch.float32)

        USE_GT = True
        if USE_GT:
            logger.info("using CSBM prior knowledge")
            y = dataset.data.y.clone().cpu()
            K = dataset.data.num_classes
            p = torch.tensor(dataset.base.p_edge_intra)
            q = torch.tensor(dataset.base.p_edge_inter)
            log_p = torch.log(p)
            log_1mp = torch.log(1 - p)
            log_q = torch.log(q)
            log_1mq = torch.log(1 - q)
            expected_pq = torch.log((p + (K - 1) * q) / K)
            expected_1mpq = torch.log(((1 - p) + (K - 1) * (1 - q)) / K)
            U = mask_train_u.nonzero().flatten().tolist()
            Q = mask_train_Q.nonzero().flatten().tolist()

            confidence_propagation = torch.zeros_like(mask_train_u, dtype=torch.float32)

            edges: Int[Tensor, "e 2"] = dataset.base.edge_indices.clone().cpu().T.tolist()
            edge_set = set(tuple(e) for e in edges) | set(tuple(e) for e in edges[::-1])
            for u in U:
                u_label = y[u]
                a_same = 0  # connected and same label
                a_diff = 0  # connected and different label
                b_same = 0  # not connected and same label
                b_diff = 0  # not connected and different label
                for v in Q:
                    v_label = y[v]
                    has_edge = (u, v) in edge_set
                    if v_label == u_label:
                        if has_edge:
                            a_same += 1
                        else:
                            b_same += 1
                    else:
                        if has_edge:
                            a_diff += 1
                        else:
                            b_diff += 1

                    cp_value = (
                        a_same * log_p
                        + b_same * log_1mp
                        + a_diff * log_q
                        + b_diff * log_1mq
                        - (a_same + a_diff) * expected_pq
                        - (b_same + b_diff) * expected_1mpq
                    )
                    confidence_propagation[v] = cp_value

            return confidence_propagation
        else:
            raise NotImplementedError("Confidence propagation is only implemented for CSBM datasets with ground truth")

    def aleatoric_confidence(
        self,
        mask_predict: Bool[Tensor, " n"],
        mask_train: Bool[Tensor, " n"],
        labels: Int[Tensor, " n"],
        model: Model,
        dataset: ActiveLearningDataset,
        model_config: ModelConfig,
        features_only: bool,
    ) -> Float[Tensor, " n"]:
        """Computes (approximate) aleatoric confidence for all nodes in `mask_predict` for a "true" label
        assignment `labels`, i.e. it treats `labels` as ground_truth."""
        if isinstance(model, SGC):
            #  For SGC, re-training can be done cheaper
            return self.aleatoric_confidence_sgc(mask_predict, mask_train, labels, model, dataset.data, features_only)

        # We need to re-train a model from scratch
        labels = labels.clone()
        labels[mask_train] = dataset.data.y[mask_train]

        if self.aleatoric_confidence_with_left_out_node:
            raise RuntimeError("Re-training a model for each node is too expensive")

        model_aleatoric = ModelFactory.create(name=model_config.name, dataset=dataset)
        logger.info("Re-training model for aleatoric uncertainty...")
        with torch.enable_grad():
            train_mask_backup, train_labels_backup = dataset.data.mask_train_l.clone(), dataset.data.y.clone()
            dataset.data.mask_train_l[:], dataset.data.y = True, labels
            AL.train_model(model_config.trainer, model_aleatoric, dataset, torch.default_generator)
            dataset.data.mask_train_l[:], dataset.data.y[:] = train_mask_backup, train_labels_backup

        prediction_aleatoric = model_aleatoric.predict(dataset.data, acquisition=True)
        probabilites = prediction_aleatoric.get_probabilities(propagated=not features_only)
        if probabilites is None:
            raise ValueError("Got no probabilities")
        aleatoric_confidence = probabilites.mean(0)[torch.arange(probabilites.size(0)), labels]
        return aleatoric_confidence

    def aleatoric_confidence_sgc(
        self,
        mask_predict: Bool[Tensor, " n"],
        mask_train: Bool[Tensor, " n"],
        labels: Int[Tensor, " n"],
        model: SGC,
        batch: GraphData,
        features_only: bool,
    ) -> Float[Tensor, " n"]:
        """Computes (approximate) aleatoric confidence for all nodes in `mask_predict` for a "true" label
        assignment `labels`, i.e. it treats `labels` as ground_truth."""
        labels = labels.clone()
        # replace the ground truth in labels when it is available
        labels[mask_train] = batch.y[mask_train]
        labels_np = labels.cpu().numpy()
        if features_only:
            x = batch.x.cpu().numpy()
        else:
            x = model.get_diffused_node_features(batch).cpu().numpy()
        aleatoric_confidence = torch.full((mask_train.size(0),), float("nan"), dtype=torch.float32)

        if self.aleatoric_confidence_with_left_out_node:
            # compute aleatoric confidence from one model trained on leaving out a node for each node
            iterator = tqdm(torch.where(mask_predict)[0]) if self.verbose else torch.where(mask_predict)[0]
            for idx in iterator:
                mask_aleatoric = np.ones_like(mask_train)
                mask_aleatoric[idx] = False
                aleatoric_confidence_idx = _probabilities_from_logistic_regression(
                    x, labels_np, mask_aleatoric, model, batch.num_classes
                )
                aleatoric_confidence[idx] = float(aleatoric_confidence_idx[idx, labels[idx]])
        else:
            # use one base model for aleatoric confidence, cheaper
            idxs = torch.where(mask_predict)[0]
            aleatoric_confidence[idxs] = torch.from_numpy(
                _probabilities_from_logistic_regression(
                    x, labels_np, np.ones_like(mask_train), model, batch.num_classes
                )[idxs, labels[idxs]]
            ).type(torch.float32)

        return aleatoric_confidence

    def epistemic_uncertainty_mp(
        self,
        mask_predict: Bool[Tensor, " n"],
        mask_train: Bool[Tensor, " n"],
        total_confidence: Float[Tensor, "n c"],
        model: Model,
        dataset: ActiveLearningDataset,
        model_config: ModelConfig,
        features_only: bool,
    ) -> Float[Tensor, " n"]:
        """Computes approximate epistemic uncertainty as the ratio aleatoric confidence / total confidence."""
        idxs_train = torch.where(mask_train)[0]
        if self.aleatoric_confidence_labels_num_samples is None:
            aleatoric_samples = total_confidence.argmax(1)[..., None]
        else:
            aleatoric_samples = torch.multinomial(
                total_confidence, self.aleatoric_confidence_labels_num_samples, replacement=True
            )

        # For the observed labels, we do not sample
        aleatoric_samples[idxs_train] = dataset.data.y[idxs_train][..., None]

        aleatoric_confidences = torch.stack(
            [
                self.aleatoric_confidence(
                    mask_predict, mask_train, aleatoric_samples[:, i], model, dataset, model_config, features_only
                )
                for i in range(aleatoric_samples.size(1))
            ],
            dim=0,
        )
        total_confidences = total_confidence[torch.arange(total_confidence.size(0)), aleatoric_samples.T]

        epistemic_uncertainties = aleatoric_confidences / (total_confidences + 1e-12)
        epistemic_uncertainty = torch.log(epistemic_uncertainties.mean(0))
        epistemic_uncertainty[~mask_predict] = -float("inf")
        print("alea conf", torch.nanmean(aleatoric_confidences), aleatoric_confidences)
        print("epi uncertainty", torch.nanmean(epistemic_uncertainty), epistemic_uncertainty)
        print("class counts", torch.unique(aleatoric_samples.flatten(), return_counts=True))

        return epistemic_uncertainty

    def epistemic_uncertainty_argmax(
        self,
        mask_predict: Bool[Tensor, " n"],
        mask_train: Bool[Tensor, " n"],
        total_confidence: Float[Tensor, "n c"],
        labels: Int[Tensor, " n"],
        model: SGC,
        batch: GraphData,
    ) -> Float[Tensor, " n"]:
        labels = labels.clone()
        labels[mask_train] = batch.y[mask_train]
        labels_np = labels.cpu().numpy()
        x = model.get_diffused_node_features(batch).cpu().numpy()
        aleatoric_confidence = torch.full((mask_train.size(0),), float("nan"), dtype=torch.float32)

        iterator = tqdm(torch.where(mask_predict)[0])

        mask_aleatoric = np.ones_like(mask_train)
        prev_idx = None
        for idx in iterator:
            mask_aleatoric[idx] = False
            if prev_idx is not None:
                mask_aleatoric[prev_idx] = True
            prev_idx = idx
            aleatoric_confidence_idx = _probabilities_from_logistic_regression(
                x, labels_np, mask_aleatoric, model, batch.num_classes
            )
            aleatoric_confidence[idx] = aleatoric_confidence_idx[idx, labels[idx]]

        epistemic_uncertainty = torch.log(
            aleatoric_confidence / total_confidence[torch.arange(total_confidence.size(0)), labels]
        )
        epistemic_uncertainty[~mask_predict] = -float("inf")
        return epistemic_uncertainty

    def epistemic_uncertainty_esp(
        self,
        mask_predict: Bool[Tensor, " n"],
        mask_train: Bool[Tensor, " n"],
        total_confidence: Float[Tensor, "n c"],
        model: SGC,
        batch: GraphData,
        features_only: bool,
    ) -> Float[Tensor, " n"]:
        """Computes approximate epistemic uncertainty as the gain in confidence in correct (=pseudo labels) predictions.

        Args:
            mask_predict: Bool[Tensor, 'n']: Mask of nodes to predict
            mask_train: Bool[Tensor, 'n']: Mask of training nodes
            total_confidence: Float[Tensor, 'n c']: Total confidence
            model: SGC: Model
            batch: Data: Batch
            features_only: bool: Whether to use only the features

        Returns:
            Float[Tensor, 'n']: The epistemic uncertainty
        """

        n, c = total_confidence.size()
        if features_only:
            x = batch.x.cpu().numpy()
        else:
            x = model.get_diffused_node_features(batch).cpu().numpy()
        mask_train_np: Bool[np.ndarray, "n"] = mask_train.cpu().numpy()
        total_confidence_np = total_confidence.cpu().numpy()
        labels_np = total_confidence_np.argmax(1)

        joint_log_probs = torch.full_like(total_confidence, -float("inf"))

        # We simplify the computation of epistemic uncertainty up to a constant factor using
        # equation (28) in our paper, (see appendix G.2)
        for i, c in tqdm(
            list(product(torch.where(mask_predict)[0], range(batch.num_classes))), disable=not self.verbose
        ):
            label_i_true = batch.y[i]
            labels_np[i] = c
            mask_train_np[i] = True
            # compute the log probability p(y_u-i = y_u-i^label | y_O, y_i=c)

            probs = _probabilities_from_logistic_regression(
                x=x, y=labels_np, mask_train=mask_train_np, model=model, num_classes=batch.num_classes
            )
            denominator_pseudo_labels = probs.argmax(1)

            joint_log_probs[i, c] = np.log(probs[np.arange(n), denominator_pseudo_labels][~mask_train_np]).sum()
            joint_log_probs[i, c] += np.log(total_confidence_np[i, int(labels_np[i])])
            labels_np[i], mask_train_np[i] = label_i_true, False

        # Now we take the expectation over the label for y_i = c weighted by the total confidence
        expected_ratios = joint_log_probs + np.log(total_confidence_np)
        expected_ratios = scipy.special.logsumexp(expected_ratios, axis=-1)
        assert not np.isnan(expected_ratios).any()
        return torch.log(torch.from_numpy(expected_ratios).float())


def _probabilities_from_logistic_regression(
    x: Float[np.ndarray, "num_nodes num_features"],
    y: Int[np.ndarray, " num_nodes"],
    mask_train: Bool[np.ndarray, " num_nodes"],
    model: SGC,
    num_classes: int,
) -> Float[np.ndarray, "num_nodes num_classes"]:
    """Computes probabilities (i.e. confidence) from fitting a logistic regression model.

    Args:
        x: Float[np.ndarray, 'num_nodes num_features']: Node features
        y: Int[np.ndarray, 'num_nodes']: Labels
        mask_train: Bool[np.ndarray, 'num_nodes']: Mask of training nodes
        model: SGC: Model
        num_classes: int: Number of classes

    Returns:
        Float[np.ndarray, 'num_nodes num_classes']: Probabilities in the predictions fit to this data.
    """
    num_nodes = y.shape[0]
    if len(set(y[mask_train])) == 1:
        # Weird "bug" in LogisticRegression that it can not fit with only one class
        # The prediction of the logistic regression classifier should be 1.0 for this one class
        probabilities = np.zeros((num_nodes, num_classes))
        probabilities[:, y[mask_train][0]] = 1.0
    else:
        # automatically determine a good solver
        solver = model.solver if mask_train.sum() <= 10000 else "saga"
        regression = LogisticRegression(
            C=model.inverse_regularization_strength,
            solver=solver,  # type: ignore
            class_weight="balanced" if model.balanced else None,
        )
        regression.fit(x[mask_train], y[mask_train])
        probabilities = regression.predict_proba(x)
        del regression
    return probabilities
