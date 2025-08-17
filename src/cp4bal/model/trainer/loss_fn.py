from abc import ABC, abstractmethod
from logging import getLogger

import torch
from jaxtyping import Float, Int
from torch import Tensor

from ..prediction import Prediction

logger = getLogger(__name__)


class Loss(ABC):
    @abstractmethod
    def __call__(self, prediction: Prediction, labels: Int[Tensor, " n"]) -> Tensor: ...


class CrossEntropyLoss(Loss):
    def __call__(self, prediction: Prediction, labels: Int[Tensor, " n"]) -> Tensor:
        logits = prediction.get_logits()
        if logits.shape[0] > 1:
            logger.warning("CrossEntropyLoss is being used with multiple samples: logits.shape=%s", logits.shape)
        logits: Float[Tensor, "n c"] = logits.mean(dim=0)
        loss = torch.nn.functional.cross_entropy(logits, labels.long())
        loss = loss.mean()
        return loss


def get_loss_function() -> Loss:
    return CrossEntropyLoss()
