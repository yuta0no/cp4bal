import torch

from cp4bal.dataset import ActiveLearningDataset

from ..base import Model
from .base import Trainer
from .configs import OracleTrainerConfig


class OracleTrainer(Trainer):
    def __init__(
        self, config: OracleTrainerConfig, model: Model, dataset: ActiveLearningDataset, generator: torch.Generator
    ):
        super().__init__(config=config, model=model, dataset=dataset, generator=generator)

    def fit(self):
        super().fit()
