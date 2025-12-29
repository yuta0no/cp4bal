import torch
from jaxtyping import Float, Int
from torch import Generator, Tensor

from cp4bal.dataset import ActiveLearningDataset
from cp4bal.model import Model, Prediction

from .base import Acquisition
from .configs import AcquisitionByAttributeConfig


class AcquisitionByAttribute(Acquisition):
    def __init__(self, config: AcquisitionByAttributeConfig):
        super().__init__(config)
        self.higher_is_better = config.higher_is_better

    def get_attribute(
            self, prediction: Prediction | None, dataset: ActiveLearningDataset, generator: Generator
        ) -> Float[Tensor, " n"]:
        raise NotImplementedError

    def select(
            self,
            model: Model,
            dataset: ActiveLearningDataset,
            budget: int,
            generator: Generator,
        ) -> Int[Tensor, " budget"]:
        if self.requires_model_predictions:
            prediction = model.predict(batch=dataset.data, acquisition=True)
        else:
            prediction = None

        attribute = self.get_attribute(prediction, dataset, generator)

        if self.higher_is_better:
            attribute[~dataset.data.mask_train_u] = float('-inf')
            selected_indices = torch.topk(attribute, k=budget).indices.tolist()
        else:
            attribute[~dataset.data.mask_train_u] = float('inf')
            selected_indices = torch.topk(-attribute, k=budget).indices.tolist()

        return selected_indices

