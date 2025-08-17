from dataclasses import dataclass

from jaxtyping import Float, Int
from torch import Tensor


@dataclass
class Prediction:
    """Represents the result of a model prediction.
    s: number of samples
    n: number of nodes
    c: number of classes
    d: dimension of embeddings
    """

    probabilities: Float[Tensor, "s n c"] | None = None

    logits: Float[Tensor, "s n c"] | None = None

    embeddings: Float[Tensor, "s n d"] | None = None

    aleatoric_confidence: Float[Tensor, "num_nodes num_classes"] | None = None
    total_confidence: Float[Tensor, "num_nodes num_classes"] | None = None

    @property
    def num_classes(self) -> int:
        """Returns the number of classes in the prediction."""
        for attr in (
            "logits",
            "probabilities",
        ):
            if getattr(self, attr) is not None:
                return getattr(self, attr).shape[-1]
            raise ValueError("Prediction does not contain logits or embeddings.")

    def get_estimated_classes(self, propagated: bool = True) -> Int[Tensor, "s n"] | None:
        """Returns the estimated classes, either propagated or unpropagated."""
        probs = self.probabilities
        if probs is not None:
            return probs.mean(dim=0).argmax(dim=-1)
        return None

    def get_logits(self) -> Float[Tensor, "s n c"] | None:
        """Returns the logits, either propagated or unpropagated."""
        return self.logits

    def get_embeddings(self) -> Float[Tensor, "s n d"] | None:
        """Returns the embeddings, either propagated or unpropagated."""
        return self.embeddings

    def get_probabilities(self) -> Float[Tensor, "s n c"] | None:
        """Returns the probabilities, either propagated or unpropagated."""
        if self.probabilities is not None:
            return self.probabilities

        if (logits := self.get_logits()) is not None:
            return logits.softmax(dim=-1)
        return None
