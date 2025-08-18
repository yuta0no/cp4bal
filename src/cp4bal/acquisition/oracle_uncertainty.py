import numpy as np
import torch

from cp4bal.dataset import CSBM, ActiveLearningDataset
from cp4bal.model import BayesOptimalModel

from .base import Acquisition
from .configs import OracleUncertaintyAcquisitionConfig
from .enums import UncertaintyType


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
                uncertainty = -1.0 * prediction.total_confidence  # considering log-likelihood
            case UncertaintyType.ALEATORIC:
                if prediction.aleatoric_confidence is None:
                    raise ValueError("Aleatoric confidence not supplied")
                uncertainty = -1.0 * prediction.aleatoric_confidence  # considering log-likelihood
            case UncertaintyType.EPISTEMIC:
                if prediction.total_confidence is None:
                    raise ValueError("Total confidence not supplied")
                if prediction.aleatoric_confidence is None:
                    raise ValueError("Aleatoric confidence not supplied")
                total_uncertainty = -1.0 * prediction.total_confidence
                aleatoric_uncertainty = -1.0 * prediction.aleatoric_confidence
                uncertainty = total_uncertainty - aleatoric_uncertainty  # considering log-likelihood
            case _:
                raise ValueError(f"Unknown uncertainty type: {self.uncertainty_type}")

        if self.confidence_propagation:
            acquired_indices = []
            # determine which to select by greedy algorithm
            for _ in range(budget):
                indices_train_u = torch.where(mask_train_u)[0]
                acquisition = uncertainty[
                    torch.arange(model.graph.num_nodes), model.graph.labels
                ]  # using oracle labels
                possible_acquisitions = acquisition[mask_train_u]
                confidence_propagation = self._compute_confidence_propagation()
                possible_acquisitions_with_cp = possible_acquisitions - confidence_propagation
                acquired_index = indices_train_u[np.argsort(-possible_acquisitions_with_cp)[0]]
                mask_train_l[acquired_index] = True
                mask_train_u[acquired_index] = False
        else:
            acquisition = uncertainty[torch.arange(model.graph.num_nodes), model.graph.labels]  # using oracle labels
            possible_acquisitions = acquisition[mask_train_u]
            acquired_indices = indices_train_u[np.argsort(-possible_acquisitions)[:budget]]
            mask_train_l[acquired_indices] = True
            mask_train_u[acquired_indices] = False

        assert (torch.unique(acquired_indices, return_counts=True)[1] == 1).all()
        assert dataset.data.mask_train_u[acquired_indices].all()

        return acquired_indices.tolist()

    def _compute_confidence_propagation(self):
        raise NotImplementedError
