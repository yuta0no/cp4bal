from logging import getLogger

import numpy as np
import torch
from jaxtyping import Bool, Float, Int
from torch import Tensor

from cp4bal.dataset import CSBM, ActiveLearningDataset
from cp4bal.model import BayesOptimalModel
from cp4bal.model.prediction import Prediction

from .base import Acquisition
from .configs import OracleUncertaintyAcquisitionConfig
from .enums import UncertaintyType

logger = getLogger(__name__)


class OracleUncertaintyAcquisition(Acquisition):
    """
    Acquisition strategy that selects samples based on the model's oracle uncertainty.
    This strategy requires the knowledge of the true labels for the unlabeled data.
    """

    def __init__(self, config: OracleUncertaintyAcquisitionConfig):
        super().__init__(config=config)
        self.confidence_propagation = config.confidence_propagation
        self.uncertainty_type = config.uncertainty_type

    @torch.no_grad()
    def select(
        self,
        model: BayesOptimalModel,
        dataset: ActiveLearningDataset,
        budget: int,
        generator: torch.Generator,
    ) -> list:
        """
        Selects a random subset of indices from the dataset.

        Args:
            model (Model): The model used for predictions (not used in random acquisition)
            dataset (ActiveLearningDataset): The dataset to select from.
            budget (int): The number of samples to select.
            generator (torch.Generator): Random number generator.

        Returns:
            list[int]: List of selected indices.
        """
        _ = generator
        if not isinstance(dataset.base, CSBM):
            raise ValueError("OracleUncertaintyAcquisition works only with CSBM")

        model.graph = dataset.base
        mask_train_l = dataset.data.mask_train_l.clone()
        mask_train_u = dataset.data.mask_train_u.clone()
        prediction = model.predict(batch=dataset.data, acquisition=True)

        match self.uncertainty_type:
            case UncertaintyType.TOTAL:
                if prediction.total_confidence is None:
                    raise ValueError("Total confidence not supplied")
                if self.confidence_propagation:
                    raise ValueError("Confidence propagation is not supported for total uncertainty")
                uncertainty = -1.0 * prediction.total_confidence  # considering log-likelihood
            case UncertaintyType.ALEATORIC:
                if prediction.aleatoric_confidence is None:
                    raise ValueError("Aleatoric confidence not supplied")
                if self.confidence_propagation:
                    raise ValueError("Confidence propagation is not supported for aleatoric uncertainty")
                uncertainty = -1.0 * prediction.aleatoric_confidence  # considering log-likelihood
            case UncertaintyType.EPISTEMIC:
                if prediction.total_confidence is None:
                    raise ValueError("Total confidence not supplied")
                if prediction.aleatoric_confidence is None:
                    raise ValueError("Aleatoric confidence not supplied")
                total_uncertainty = -torch.log(prediction.total_confidence + 1e-12)
                aleatoric_uncertainty = -torch.log(prediction.aleatoric_confidence + 1e-12)
                uncertainty = total_uncertainty - aleatoric_uncertainty  # considering log-likelihood
            case _:
                raise ValueError(f"Unknown uncertainty type: {self.uncertainty_type}")

        if self.confidence_propagation:
            acquired_indices = []
            mask_train_Q = torch.zeros_like(mask_train_l, dtype=torch.bool)
            for _ in range(budget):
                # determine which to select by greedy algorithm
                cp = self._calculate_confidence_propagation(
                    mask_train_u=mask_train_u,
                    mask_train_Q=mask_train_Q,
                    dataset=dataset,
                    prediction=prediction,
                )
                values_for_acquisition = uncertainty - cp
                indices_train_u = torch.where(mask_train_u)[0]
                values_for_acquisition = values_for_acquisition[
                    torch.arange(model.graph.num_nodes), model.graph.labels
                ]  # using oracle labels
                possible_values_for_acquisition = values_for_acquisition[mask_train_u]
                acquired_index = indices_train_u[np.argsort(possible_values_for_acquisition)[-1]]
                mask_train_Q[acquired_index] = True
                mask_train_u[acquired_index] = False
                acquired_indices.append(acquired_index.item())
            acquired_indices = torch.tensor(acquired_indices, dtype=int)
        else:
            indices_train_u = torch.where(mask_train_u)[0]
            acquisition = uncertainty[torch.arange(model.graph.num_nodes), model.graph.labels]  # using oracle labels
            possible_acquisitions = acquisition[mask_train_u]
            acquired_indices = indices_train_u[np.argsort(possible_acquisitions)[-budget:]]
            mask_train_l[acquired_indices] = True
            mask_train_u[acquired_indices] = False

        assert (torch.unique(acquired_indices, return_counts=True)[1] == 1).all()
        assert dataset.data.mask_train_u[acquired_indices].all()

        return acquired_indices.tolist()

    def _calculate_confidence_propagation(
        self,
        mask_train_u: Bool[Tensor, " n"],
        mask_train_Q: Bool[Tensor, " n"],
        dataset: ActiveLearningDataset,
        prediction: Prediction,
    ) -> Float[Tensor, "n 1"]:
        if not isinstance(dataset.base, CSBM):
            raise ValueError("Confidence propagation is only implemented for CSBM datasets")

        if mask_train_Q.sum() == 0:
            # no propagation for empty Q
            return torch.zeros_like(mask_train_u, dtype=torch.float32)[:, None]

        USE_GT_LABEL = True
        if USE_GT_LABEL:
            logger.info("using ground-truth labels for confidence propagation")
            y = dataset.data.y.clone().cpu()
        else:
            logger.info("using predicted labels for confidence propagation")
            y = prediction.probabilities.mean(dim=0).argmax(dim=-1)

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
            confidence_propagation[u] = cp_value

        return confidence_propagation[:, None]
