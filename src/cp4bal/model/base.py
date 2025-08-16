from abc import abstractmethod

import torch.nn as nn

from cp4bal.dataset import ActiveLearningDataset, GraphData
from cp4bal.model import Prediction
from cp4bal.util.configs import (
    MCDropoutModelConfig,
    ModelConfig,
    MultipleSampleModelConfig,
)


class Model(nn.Module):
    def __init__(self, config: ModelConfig, dataset: ActiveLearningDataset):
        super().__init__()
        self.name = config.name

    @abstractmethod
    def reset_parameters(self): ...

    @abstractmethod
    def predict(self, batch: GraphData, acquisition: bool = False) -> Prediction: ...


class MultipleSampleModel(Model):
    """Base model class for models that can sample multiple predictions probabilistically."""

    def __init__(self, config: MultipleSampleModelConfig, dataset: ActiveLearningDataset):
        super().__init__(config, dataset)
        self.num_samples_eval = config.num_samples_eval
        self.num_samples_train = config.num_samples_train

    @abstractmethod
    def predict_multiple(self, batch: GraphData, num_samples: int, acquisition: bool = False) -> Prediction: ...

    def predict(self, batch: GraphData, acquisition: bool = False) -> Prediction:
        num_samples = self.num_samples_train if self.training else self.num_samples_eval
        return self.predict_multiple(batch, num_samples, acquisition=acquisition)

    @property
    def prediction_changes_at_eval(self) -> bool:
        return True


class MCDropoutModel(MultipleSampleModel):
    """Monte Carlo Dropout Model."""

    def __init__(self, config: MCDropoutModelConfig, dataset: ActiveLearningDataset):
        super().__init__(config, dataset)
        self.dropout_p: float = config.dropout_p
        self.dropout_at_eval: bool = config.dropout_at_eval
