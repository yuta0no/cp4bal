import torch
from jaxtyping import Float
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Prediction

from .attribute import AcquisitionByAttribute
from .configs import LeastConfidenceAcquisitionConfig


class LeastConfidenceAcquisition(AcquisitionByAttribute):
    def __init__(self, config: LeastConfidenceAcquisitionConfig):
        super().__init__(config)

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        _ = dataset, generator

        if prediction is None:
            raise ValueError("Model predictions are required for LeastConfidenceAcquisition.")

        probabilities: Float[Tensor, " s n c"] = prediction.probabilities
        margin = (1 - probabilities.sort(dim=-1).values[:, :, 0]).mean(dim=0)
        return margin
