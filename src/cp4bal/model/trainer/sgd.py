import torch

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model
from cp4bal.model.trainer.base import Trainer
from cp4bal.util.configs import SGDTrainerConfig


class SGDTrainer(Trainer):
    def __init__(self, config: SGDTrainerConfig, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator):
        super().__init__(config, model, dataset, rg)

    def fit(self, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator):
        """Fits the model to a dataset.

        Args:
            model (BaseModel): The model to fit
            dataset (Dataset): The dataset to fit to
            generator (torch.Generator): A random number generator
        """
        super().fit(model, dataset, rg)
