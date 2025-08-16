from logging import getLogger
from typing import Any, Callable, Sequence, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch_geometric.nn as tgnn
from jaxtyping import Float, Int
from torch import Tensor

from cp4bal.dataset import ActiveLearningDataset, GraphData
from cp4bal.model import MCDropoutModel, Prediction
from cp4bal.util.configs import GCNConfig

logger = getLogger(__name__)


class GCN(MCDropoutModel):
    def __init__(self, config: GCNConfig, dataset: ActiveLearningDataset):
        super().__init__(config, dataset)
        self.inplace = config.inplace
        self.layers = nn.ModuleList()
        in_dim = dataset.num_input_features
        for out_dim in list(config.hidden_dims) + [dataset.data.num_classes]:
            self.layers.append(
                tgnn.GCNConv(
                    in_dim,
                    out_dim,
                    improved=config.improved,
                    cached=config.cached,
                    add_self_loops=config.add_self_loops,
                )
            )
            in_dim = out_dim

    def reset_parameters(self):
        for layer in self.layers:
            layer.reset_parameters()

    def forward_impl(
        self,
        x: Float[Tensor, "num_nodes feature_dim"],
        edge_index: Int[Tensor, "2 num_edges"] | None,
        edge_weight: Int[Tensor, "num_edges 1"] | None = None,
        acquisition: bool = False,
    ) -> Tuple[
        Float[Tensor, "num_nodes embedding_dim"] | None,
        Float[Tensor, "num_nodes num_classes"],
    ]:
        embedding = None
        for layer_idx, layer in enumerate(self.layers):
            if edge_index is None:
                x = layer.lin(x)
            else:
                x = layer(x, edge_index, edge_weight)
            if acquisition and layer_idx == len(self.layers) - 2:  # only return an embedding when doing acquisition
                embedding = x
            if layer_idx != len(self.layers) - 1:
                x = F.relu(x, inplace=self.inplace)
                if self.dropout_p:
                    x = F.dropout(
                        x,
                        p=self.dropout_p,
                        inplace=self.inplace and not acquisition,
                        training=self.training or self.dropout_at_eval,
                    )
        return embedding, x

    @property
    def prediction_changes_at_eval(self):
        return self.dropout_p > 0

    def forward(
        self, batch: GraphData, acquisition: bool = False
    ) -> Tuple[
        Float[Tensor, "num_nodes embedding_dim"] | None,
        Float[Tensor, "num_nodes embedding_dim"] | None,
        Float[Tensor, "num_nodes num_classes"],
        Float[Tensor, "num_nodes num_classes"] | None,
    ]:
        embeddings, logits = self.forward_impl(batch.x, batch.edge_index, batch.edge_attr, acquisition=acquisition)
        if acquisition:
            embeddings_unpropagated, logits_unpropagated = self.forward_impl(
                batch.x, edge_index=None, edge_weight=None, acquisition=acquisition
            )
        else:
            embeddings_unpropagated, logits_unpropagated = None, None
        return embeddings, embeddings_unpropagated, logits, logits_unpropagated

    def predict_multiple_iterative(self, batch: GraphData, num_samples: int, acquisition: bool = False) -> Prediction:
        """Predicts multiple samples by iteratively using `self.forward`"""
        embeddings, logits = map(
            lambda tensors: apply_to_optional_tensors(torch.stack, tensors),  # type: ignore
            zip(*[self(batch, acquisition=acquisition) for _ in range(num_samples)]),
        )
        return Prediction(
            logits=logits,
            embeddings=embeddings,
        )

    def predict_multiple(self, batch: GraphData, num_samples: int, acquisition: bool = False) -> Prediction:
        return self.predict_multiple_iterative(batch, num_samples, acquisition=acquisition)


def apply_to_optional_tensors(fn: Callable, tensors: Sequence[Tensor | None]) -> Any | None:
    """Applies a function to a sequence of optional tensors."""
    if not (all(tensor is None for tensor in tensors) or all(tensor is not None for tensor in tensors)):
        raise ValueError("Sequence of optional tensors must be homogenous w.r.t. being None")
    if len(tensors) == 0 or tensors[0] is None:
        return None
    else:
        return fn(tensors)
