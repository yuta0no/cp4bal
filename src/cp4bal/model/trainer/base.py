import torch

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model
from cp4bal.util.configs import TrainerConfig


class Trainer:
    """Base class for model training."""

    def __init__(self, config: TrainerConfig, model: Model, dataset: ActiveLearningDataset, generator: torch.Generator):
        self.verbose = config.verbose

    def fit(self, model: Model, dataset: ActiveLearningDataset, generator: torch.Generator) -> None:
        """Fits the model to a dataset.

        Args:
            model (BaseModel): The model to fit
            dataset (Dataset): The dataset to fit to
            generator (torch.Generator): A random number generator
        """
        ...

    def transfer_model_to_device(self, model: Model) -> Model:
        return model

    def transfer_dataset_to_device(self, dataset: ActiveLearningDataset) -> ActiveLearningDataset:
        return dataset
