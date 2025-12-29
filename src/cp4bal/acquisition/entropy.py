import torch
from jaxtyping import Float
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Prediction

from .attribute import AcquisitionByAttribute
from .configs import AcquisitionByAttributeConfig


class EntropyAcquisition(AcquisitionByAttribute):
    def __init__(self, config: AcquisitionByAttributeConfig):
        super().__init__(config)

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        _ = dataset, generator

        if prediction is None:
            raise ValueError("Model predictions are required for EntropyAcquisition.")

        probabilities: Float[Tensor, " s n c"] = prediction.probabilities
        log_probabilities = torch.log(probabilities + 1e-12)
        print(log_probabilities.shape)
        entropy = -torch.sum(probabilities * log_probabilities, dim=2).mean(dim=0)  # reduce over samples

        return entropy