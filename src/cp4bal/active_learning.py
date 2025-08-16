from logging import getLogger

import torch
import torch.nn.functional as F
from jaxtyping import Float
from torch import Tensor

from cp4bal.acquisition import Acquisition
from cp4bal.dataset import ActiveLearningDataset, GraphData
from cp4bal.model import Model, Prediction
from cp4bal.model.trainer import Trainer, TrainerFactory
from cp4bal.util.configs import ActiveLearningConfig, TrainerConfig
from cp4bal.util.enums import DatasetSplit

logger = getLogger(__name__)


class ActiveLearning:
    @staticmethod
    def acquire_samples(
        config: ActiveLearningConfig,
        model: Model,
        acquisition: Acquisition,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        al_round: int = -1,
    ):
        num_nodes_before = dataset.num_train_labeled_nodes
        selected = acquisition.select(model=model, dataset=dataset, budget=config.budget_per_round, generator=rg)
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
        if config.reset_parameter_before_training:
            model.reset_parameters()
        trainer: Trainer = TrainerFactory.create(config=config, model=model, dataset=dataset, rg=rg)
        trainer.fit(model=model, dataset=dataset, rg=rg)

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
            logits: Float[Tensor, "s n c"] = prediction.get_logits(propagated=True)
            logits: Float[Tensor, "n c"] = logits.mean(dim=0)
            mask = dataset.data.get_mask(which=which)
            acc = (logits[mask].argmax(dim=-1) == dataset.data.y[mask]).float().mean()
        logger.info(f"Accuracy ({which.name}): {acc:.4f}")
        return acc

    @staticmethod
    def train_epoch(
        optimizer: torch.optim.Optimizer,
        model: Model,
        dataset: ActiveLearningDataset,
        epoch_idx: int,
        rg: torch.Generator,
    ):
        model.train()
        optimizer.zero_grad()
        batch = dataset.data
        prediction: Prediction = model.predict(batch)
        loss = compute_loss(prediction=prediction, batch=batch, which=DatasetSplit.TRAIN_L)
        loss.backward()
        optimizer.step()
        return loss.item()


def compute_loss(prediction: Prediction, batch: GraphData, which: DatasetSplit) -> Tensor:
    logits: Float[Tensor, "s n c"] = prediction.get_logits(propagated=True)  # TODO
    logits: Float[Tensor, "n c"] = logits.mean(dim=0)
    mask = batch.get_mask(which=which)
    loss = F.cross_entropy(logits[mask], batch.y[mask], reduction="none")
    return loss.mean()
