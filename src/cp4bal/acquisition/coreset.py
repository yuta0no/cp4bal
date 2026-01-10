import torch
from jaxtyping import Int
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model, Prediction

from .attribute import Acquisition
from .configs import CoresetAcquisitionConfig
from .enums import CoresetDistance


class CoresetAcquisition(Acquisition):
    def __init__(self, config: CoresetAcquisitionConfig):
        super().__init__(config)
        self.coreset_distance = config.coreset_distance

    def _get_features(self, dataset: ActiveLearningDataset, prediction: Prediction | None) -> Tensor:
        match self.coreset_distance:
            case CoresetDistance.INPUT_FEATURES:
                return dataset.data.x
            case CoresetDistance.LATENT_FEATURES:
                raise NotImplementedError("Latent features distance is not implemented yet.")
            case CoresetDistance.APPR:
                raise NotImplementedError("APPR distance is not implemented yet.")
            case _:
                raise ValueError(f"Unsupported coreset distance type: {self.coreset_distance}")

    def _greedy_k_center(
        self,
        unlabeled_indices: Tensor,
        unlabeled_features: Tensor,
        labeled_features: Tensor,
        budget: int,
    ) -> Int[Tensor, " budget"]:
        selected_indices = []
        distances = torch.cdist(unlabeled_features, labeled_features).min(dim=1).values

        for _ in range(budget):
            next_rel_index = torch.argmax(distances).item()
            next_index = unlabeled_indices[next_rel_index]
            selected_indices.append(next_index)

            new_distances = torch.cdist(
                unlabeled_features,
                unlabeled_features[next_rel_index].unsqueeze(0)
            ).squeeze(1)
            distances = torch.minimum(distances, new_distances)

        return torch.tensor(selected_indices, dtype=torch.long)

    def select(
        self,
        model: Model,
        dataset: ActiveLearningDataset,
        budget: int,
        generator: Generator,
    ) -> Int[Tensor, " budget"]:
        mask_l = dataset.data.mask_train_l
        mask_u = dataset.data.mask_train_u

        if mask_l.sum() == 0:
            # If there are no labeled nodes, select random nodes
            all_indices = torch.arange(dataset.num_nodes)
            selected_indices = all_indices[mask_u]
            selected_indices = selected_indices[torch.randperm(len(selected_indices), generator=generator)[:budget]]
            return selected_indices

        features = self._get_features(dataset, None)
        unlabeled_features = features[mask_u]
        labeled_features = features[mask_l]
        return self._greedy_k_center(
            unlabeled_indices=torch.arange(dataset.num_nodes)[mask_u],
            unlabeled_features=unlabeled_features,
            labeled_features=labeled_features,
            budget=budget,
        )
