import torch
from jaxtyping import Float
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Prediction

from .attribute import AcquisitionByAttribute
from .configs import MarginAcquisitionConfig


class MarginAcquisition(AcquisitionByAttribute):
    def __init__(self, config: MarginAcquisitionConfig):
        super().__init__(config)

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        _ = dataset, generator

        if prediction is None:
            raise ValueError("Model predictions are required for MarginAcquisition.")

        probabilities: Float[Tensor, " s n c"] = prediction.probabilities
        margin = (probabilities.sort(dim=-1).values[:, :, -1] - probabilities.sort(dim=-1).values[:, :, -2]).mean(dim=0)
        return margin
