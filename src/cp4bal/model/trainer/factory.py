from logging import getLogger

import torch

from cp4bal.dataset import ActiveLearningDataset

from ..base import Model
from .adam import AdamTrainer
from .base import Trainer
from .configs import AdamTrainerConfig, OracleTrainerConfig, SGCTrainerConfig, TrainerConfig
from .enums import TrainerType
from .gt_trainer import OracleTrainer
from .sgc import SGCTrainer

logger = getLogger(__name__)


class TrainerFactory:
    @staticmethod
    def create(config: TrainerConfig, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator) -> Trainer:
        match config.name:
            case TrainerType.ADAM:
                if not isinstance(config, AdamTrainerConfig):
                    raise ValueError(f"invalid config for AdamTrainer: {config}")
                return AdamTrainer(config=config, model=model, dataset=dataset, generator=rg)
            case TrainerType.ORACLE:
                if not isinstance(config, OracleTrainerConfig):
                    raise ValueError(f"invalid config for OracleTrainer: {config}")
                return OracleTrainer(config=config, model=model, dataset=dataset, generator=rg)
            case TrainerType.SGC:
                if not isinstance(config, SGCTrainerConfig):
                    raise ValueError(f"invalid config for SGCTrainer: {config}")
                return SGCTrainer(config=config, model=model, dataset=dataset, generator=rg)
            case _:
                raise ValueError(f"unknown trainer type: {config.name.lower()}")
