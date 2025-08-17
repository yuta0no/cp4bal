from logging import getLogger

import torch
import torch.optim as optim

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model
from cp4bal.model.trainer.base import Trainer
from cp4bal.model.trainer.loss_fn import get_loss_function
from cp4bal.util.configs import AdamTrainerConfig

logger = getLogger(__name__)


class AdamTrainer(Trainer):
    def __init__(self, config: AdamTrainerConfig, model: Model, dataset: ActiveLearningDataset, rg: torch.Generator):
        super().__init__(config, model, dataset, rg)

        self.dataset = dataset
        self.model = model
        self.config = config
        self.rg = rg

        self.loss_fn = get_loss_function()
        self.optimizer = self._get_optimizer(config.lr, config.weight_decay)

    def fit(self):
        """Fits the model to a dataset."""
        model = self.transfer_model_to_device(self.model)
        dataset = self.transfer_dataset_to_device(self.dataset)

        for epoch in range(self.config.max_epochs):
            metrics = self._train_one_epoch(epoch, model, dataset)
            logger.info(metrics)

    def _train_one_epoch(self, epoch: int, model: Model, dataset: ActiveLearningDataset) -> dict[str, float]:
        model.train()
        batch = dataset.data
        self.optimizer.zero_grad()
        prediction = model.predict(batch=batch, acquisition=False)
        loss = self.loss_fn(prediction, batch.y)
        loss.backward()
        self.optimizer.step()
        return {
            "epoch": epoch,
            "phase": "train",
            "loss": loss.item(),
        }

    def _get_optimizer(self, lr: float, weight_decay: float):
        return optim.Adam(self.model.parameters(), lr=lr, weight_decay=weight_decay)
