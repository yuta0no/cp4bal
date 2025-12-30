import torch
from jaxtyping import Float
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Prediction

from .attribute import AcquisitionByAttribute
from .configs import DegreeAcquisitionConfig
from .enums import DegreeType


class DegreeAcquisition(AcquisitionByAttribute):
    def __init__(self, config: DegreeAcquisitionConfig):
        super().__init__(config)
        self.degree_type = config.degree_type

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        _ = generator, prediction

        match self.degree_type:
            case DegreeType.IN:
                return dataset.node_degrees_in
            case DegreeType.OUT:
                return dataset.node_degrees_out
            case _:
                raise ValueError(f"Unsupported degree type: {self.degree_type}")
