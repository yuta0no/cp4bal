import torch

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model
from cp4bal.model.trainer import AdamTrainer, Trainer
from cp4bal.util.configs import AdamTrainerConfig, TrainerConfig


class TrainerFactory:
    @staticmethod
    def create(config: TrainerConfig, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator) -> Trainer:
        match config.name.lower():
            case "adam":
                if not isinstance(config, AdamTrainerConfig):
                    raise ValueError(f"invalid config for AdamTrainer: {config}")
                return AdamTrainer(config=config, model=model, dataset=dataset, rg=rg)
            case _:
                raise ValueError(f"unknown trainer type: {config.name.lower()}")
