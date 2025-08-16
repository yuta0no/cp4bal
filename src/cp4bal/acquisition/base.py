from abc import ABC, abstractmethod

from jaxtyping import Int
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model

from .configs import AcquisitionConfig


class Acquisition(ABC):
    def __init__(self, config: AcquisitionConfig):
        self.type_ = config.type_
        self.requires_model_predictions = config.requires_model_predictions

    @abstractmethod
    def select(
        self,
        model: Model,
        dataset: ActiveLearningDataset,
        budget: int,
        generator: Generator,
    ) -> Int[Tensor, " budget"]:
        pass
