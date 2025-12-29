import torch
from jaxtyping import Float
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Prediction

from .attribute import AcquisitionByAttribute
from .configs import EnergyAcquisitionConfig


class EnergyAcquisition(AcquisitionByAttribute):
    def __init__(self, config: EnergyAcquisitionConfig):
        super().__init__(config)
        self.temperature = config.temperature

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        _ = dataset, generator

        if prediction is None:
            raise ValueError("model predictions are required for EnergyAcquisition.")

        logits = prediction.get_logits()
        if logits is None:
            raise ValueError("logits are required for EnergyAcquisition.")

        energy = -self.temperature * torch.logsumexp(logits / self.temperature, dim=-1).mean(dim=0)

        return energy