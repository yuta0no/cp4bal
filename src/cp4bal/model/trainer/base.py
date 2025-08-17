from abc import abstractmethod

import torch

from cp4bal.dataset import ActiveLearningDataset

from ..base import Model
from .configs import TrainerConfig


class Trainer:
    """Base class for model training."""

    def __init__(self, config: TrainerConfig, model: Model, dataset: ActiveLearningDataset, generator: torch.Generator):
        self.config = config
        self.model = model
        self.dataset = dataset
        self.generator = generator
        self.verbose = config.verbose

    @abstractmethod
    def fit(self) -> None:
        """Fits the model to a dataset"""
        ...

    def transfer_model_to_device(self, model: Model) -> Model:
        if self.config.use_gpu and torch.cuda.is_available():
            model = model.cuda()
        return model

    def transfer_dataset_to_device(self, dataset: ActiveLearningDataset) -> ActiveLearningDataset:
        if self.config.use_gpu and torch.cuda.is_available():
            dataset = dataset.cuda()
        return dataset
