import torch

from .base import Acquisition
from .configs import RandomAcquisitionConfig


class RandomAcquisition(Acquisition):
    """
    Random acquisition strategy that selects samples randomly from the dataset.
    """

    def __init__(self, config: RandomAcquisitionConfig = RandomAcquisitionConfig()):
        super().__init__(config=config)

    def select(self, model, dataset, budget, generator):
        """
        Selects a random subset of indices from the dataset.

        Args:
            model (Model): The model used for predictions (not used in random acquisition)
            dataset (ActiveLearningDataset): The dataset to select from.
            budget (int): The number of samples to select.
            generator (torch.Generator): Random number generator.

        Returns:
            list: List of selected indices.
        """
        _ = model
        candidate_indices = dataset.data.mask_train_u.nonzero().ravel().cpu()
        p = torch.ones_like(candidate_indices) / len(candidate_indices)
        selected_indices = candidate_indices[p.multinomial(num_samples=budget, replacement=False, generator=generator)]
        return selected_indices.tolist()
