from logging import getLogger

import torch
from jaxtyping import Float
from torch import Tensor

from cp4bal.acquisition import Acquisition
from cp4bal.dataset import ActiveLearningDataset, DatasetSplit
from cp4bal.model import Model, Prediction
from cp4bal.model.trainer.base import Trainer, TrainerConfig
from cp4bal.model.trainer.factory import TrainerFactory
from cp4bal.util.writer import Writer

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
        trainer_config: TrainerConfig,
        model: Model,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        al_round: int = -1,
    ):
        logger.info(f"{dataset.data.mask_train_l.sum().item()=}")
        if dataset.data.mask_train_l.sum().item() <= 0:
            return

        _ = al_round
        if trainer_config.reset_parameter_before_training:
            logger.info("resetting model parameters before training")
            model.reset_parameters()
        trainer: Trainer = TrainerFactory.create(config=trainer_config, model=model, dataset=dataset, rg=rg)
        trainer.fit()

    @staticmethod
    def evaluate_model(
        model: Model,
        dataset: ActiveLearningDataset,
        rg: torch.Generator,
        which: DatasetSplit,
        al_round: int = -1,
        writer: Writer | None = None,
    ) -> float:
        model.eval()
        _ = rg, al_round
        with torch.no_grad():
            prediction: Prediction = model.predict(dataset.data)
            mask = dataset.data.get_mask(which=which)
            if mask.sum().item() == 0:
                logger.warning(f"No nodes in the {which} set.")
                return -1.0
            acc = 0.0
            if (logits := prediction.get_logits()) is not None:
                logits: Float[Tensor, "n c"] = logits.mean(dim=0)
                acc = (logits[mask].argmax(dim=-1) == dataset.data.y[mask]).float().mean().item()
            elif (probs := prediction.get_probabilities()) is not None:
                probs: Float[Tensor, "n c"] = probs.mean(dim=0)
                acc = (probs[mask].argmax(dim=-1) == dataset.data.y[mask]).float().mean().item()
            else:
                raise RuntimeError("Neither logits nor probabilities are available for evaluation")

            logger.info(f"Accuracy ({which.name}): {acc:.4f}")
            if writer is not None:
                writer.write(
                    {
                        "round": al_round,
                        "phase": which.name,
                        "num_labeled_nodes": dataset.num_train_labeled_nodes,
                        "accuracy": acc,
                    }
                )
        return acc
