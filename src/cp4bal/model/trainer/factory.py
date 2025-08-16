import torch

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model
from cp4bal.model.trainer import Trainer


class TrainerFactory:
    @staticmethod
    def create(trainer_type: str, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator) -> Trainer:
        match trainer_type.lower():
            case "sgd":
                raise NotImplementedError
            case _:
                raise ValueError(f"Unknown trainer type: {trainer_type}. Supported types: 'oracle', 'sgd'.")
