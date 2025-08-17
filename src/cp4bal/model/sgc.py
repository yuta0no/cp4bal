from logging import getLogger

import numpy as np
import torch
from jaxtyping import Float
from sklearn.exceptions import NotFittedError
from sklearn.linear_model import LogisticRegression

from cp4bal.dataset import ActiveLearningDataset, GraphData
from cp4bal.util.configs import SGCConfig

from .base import Model
from .prediction import Prediction

logger = getLogger(__name__)


class SGC(Model):
    """Uses the simplified graph convolution framework: p = sigma(A^(k)XW)"""

    def __init__(self, config: SGCConfig, dataset: ActiveLearningDataset):
        super().__init__(config, dataset)
        self.inverse_regularization_strength = config.inverse_regularization_strength
        self.cached = config.cached
        self.balanced = config.balanced
        self.normalize = True
        self.add_self_loops = config.add_self_loops
        self.improved = config.improved
        self.k = config.k

        self.reset_cache()
        self._frozen_prediction = None
        self.reset_parameters()

    def reset_cache(self):
        self._cached_node_features = None

    def reset_parameters(self):
        self.logistic_regression = LogisticRegression(
            C=self.inverse_regularization_strength, solver="saga", class_weight="balanced"
        )
        self._frozen_prediction = None

    @torch.no_grad()
    def predict(self, batch: GraphData, acquisition: bool = False) -> Prediction:
        if isinstance(self._frozen_prediction, int):  # Prediction is frozen to this one class
            probs = np.zeros((batch.num_nodes, batch.num_classes), dtype=float)  # type: ignore
            probs[:, self._frozen_prediction] = 1.0
            probs, probs_unpropagated = probs, probs
            logits, logits_unpropagated = probs, probs_unpropagated  # a bit arbitrary...
        else:
            if self.logistic_regression is None:
                raise RuntimeError("no regression model was fitted for SGC")
            try:
                x = self.get_diffused_node_features(batch)
                probs = self.logistic_regression.predict_proba(x)
                probs_unpropagated = self.logistic_regression.predict_proba(batch.x.cpu().numpy())
                logits = self.logistic_regression.decision_function(x)
                logits_unpropagated = self.logistic_regression.decision_function(batch.x.cpu().numpy())
            except NotFittedError:
                logger.warning("predictions with a non-fitted regression model: Fall back to uniform predictions")
                probs = np.ones((batch.num_nodes, batch.num_classes), dtype=float) / batch.num_classes  # type: ignore
                probs, probs_unpropagated = probs, probs
                logits, logits_unpropagated = probs, probs_unpropagated  # a bit arbitrary...
        _ = logits_unpropagated
        return Prediction(
            probabilities=torch.from_numpy(probs[None, ...]),
            logits=torch.from_numpy(logits[None, ...]),
            embeddings=torch.from_numpy(logits[None, ...]),
        )

    @torch.no_grad()
    def get_diffused_node_features(self, batch: GraphData) -> Float[torch.Tensor, "num_nodes num_features"]:
        """Gets the diffused node features."""
        return batch.get_diffused_node_features(
            self.k, normalize=self.normalize, improved=self.improved, add_self_loops=self.add_self_loops, cache=True
        )

    def freeze_predictions(self, class_idx: int):
        self._frozen_prediction = class_idx

    def unfreeze_predictions(self):
        self._frozen_prediction = None
