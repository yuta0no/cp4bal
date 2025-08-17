from logging import getLogger

import torch
from jaxtyping import Float
from torch import Tensor

from cp4bal.acquisition import Acquisition
from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model, Prediction
from cp4bal.model.trainer import Trainer, TrainerFactory
from cp4bal.util.configs import TrainerConfig
from cp4bal.util.enums import DatasetSplit

logger = getLogger(__name__)


class ActiveLearning:
    @staticmethod
    def acquire_samples(
        budget: int,
        model: Model,
        acquisition: Acquisition,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        al_round: int = -1,
    ):
        num_nodes_before = dataset.num_train_labeled_nodes
        selected = acquisition.select(model=model, dataset=dataset, budget=budget, generator=rg)
        logger.info(f"Round {al_round + 1}: Selected samples {selected}")
        dataset.add_to_train_labeled_indices(selected)
        logger.info(
            "#train labeled nodes: %d -> %d",
            num_nodes_before,
            dataset.num_train_labeled_nodes,
        )
        return dataset

    @staticmethod
    def train_model(
        config: TrainerConfig,
        model: Model,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        al_round: int = -1,
    ):
        _ = al_round
        if config.reset_parameter_before_training:
            model.reset_parameters()
        trainer: Trainer = TrainerFactory.create(config=config, model=model, dataset=dataset, rg=rg)
        trainer.fit()

    @staticmethod
    def evaluate_model(
        model: Model,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        which: DatasetSplit,
        al_round: int = -1,
    ):
        model.eval()
        _ = rg, al_round
        with torch.no_grad():
            prediction: Prediction = model.predict(dataset.data)
            logits: Float[Tensor, "s n c"] = prediction.get_logits()
            logits: Float[Tensor, "n c"] = logits.mean(dim=0)
            mask = dataset.data.get_mask(which=which)
            acc = (logits[mask].argmax(dim=-1) == dataset.data.y[mask]).float().mean()
        logger.info(f"Accuracy ({which.name}): {acc:.4f}")
        return acc
