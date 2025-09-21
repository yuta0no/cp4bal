from logging import getLogger
from pathlib import Path
from typing import Self

import torch
import torch_geometric.nn as tgnn
import torch_scatter
from jaxtyping import Bool, Float, Int
from torch import Tensor
from torch.utils.data import Dataset as TorchDataset
from torch_geometric.data import Data as TorchGeometricData

from .configs import DatasetConfig
from .enums import DatasetSplit, InitialPoolSelectionType

logger = getLogger(__name__)


class GraphDataset:
    def __init__(
        self,
        node_features: Float[Tensor, "num_nodes dim_features"],
        labels: Float[Tensor, " num_nodes"],
        edge_indices: Int[Tensor, "2 num_edges"],
        num_classes: int | None = None,
        mask_train: Bool[Tensor, " num_nodes"] | None = None,
        mask_val: Bool[Tensor, " num_nodes"] | None = None,
        mask_test: Bool[Tensor, " num_nodes"] | None = None,
    ):
        self.node_features = node_features
        self.labels = labels
        self.edge_indices = edge_indices
        if num_classes is None:
            self.num_classes = len(set(labels))
        else:
            self.num_classes = num_classes
        self.mask_train = mask_train
        self.mask_val = mask_val
        self.mask_test = mask_test

        logger.info(
            f"Average node degree: out={self.node_degrees_out.mean().item():.4f}, "
            f"in={self.node_degrees_in.mean().item():.4f}"
        )

    @property
    def node_degrees_in(self) -> Int[Tensor, "num_nodes"]:
        return torch_scatter.scatter_add(torch.ones(self.edge_indices.size(1)), self.edge_indices[1])

    @property
    def node_degrees_out(self) -> Int[Tensor, "num_nodes"]:
        return torch_scatter.scatter_add(torch.ones(self.edge_indices.size(1)), self.edge_indices[0])

    @property
    def num_nodes(self) -> int:
        return self.node_features.size(0)

    @property
    def num_edges(self) -> int:
        return self.edge_indices.size(1)

    @property
    def dim_features(self) -> int:
        return self.node_features.size(1)

    @property
    def edge_homophily_ratio(self) -> Float[Tensor, " 1"]:
        """Computes the edge homophily ratio, i.e. the ratio of edges that connect nodes of the same class."""
        if self.edge_indices.size(1) == 0:
            return torch.tensor(0.0, device=self.edge_indices.device)
        same_class_edges = (self.labels[self.edge_indices[0]] == self.labels[self.edge_indices[1]]).sum()
        return same_class_edges.float() / self.edge_indices.size(1)

    def plot_graph_structure(self, save_path: Path):
        """Plots the graph structure using networkx."""
        import matplotlib.pyplot as plt
        import networkx as nx

        logger.debug("======")
        logger.debug(len(self.labels))
        logger.debug(self.edge_indices.shape[1])

        G = nx.Graph()
        G.add_edges_from(self.edge_indices.T.cpu().numpy())
        pos = nx.spring_layout(G)
        logger.debug(f"Number of nodes: {G.number_of_nodes()}")
        logger.debug(f"Number of edges: {G.number_of_edges()}")
        logger.debug("======")
        nx.draw(
            G,
            pos,
            with_labels=False,
            node_color=self.labels.cpu().numpy(),
            cmap=plt.cm.tab10,
        )
        plt.savefig(save_path)


class GraphData(TorchGeometricData):
    """A graph data instance."""

    def __init__(
        self,
        x: Float[Tensor, "num_nodes dim_features"],
        y: Float[Tensor, " num_nodes"],
        edge_index: Int[Tensor, "2 num_edges"],
        mask_test: Bool[Tensor, " num_nodes"],
        num_classes: int,
    ):
        mask_train_u: Bool[Tensor, " num_nodes"] = torch.ones_like(y, dtype=torch.bool) & ~mask_test
        mask_train_l: Bool[Tensor, " num_nodes"] = torch.zeros_like(y, dtype=torch.bool)
        mask_val: Bool[Tensor, " num_nodes"] = torch.zeros_like(y, dtype=torch.bool)

        super().__init__(
            x=x,
            edge_index=edge_index,
            y=y,
            # kwargs
            num_classes=num_classes,
            mask_train_u=mask_train_u,
            mask_train_l=mask_train_l,
            mask_val=mask_val,
            mask_test=mask_test,
        )

        self.num_classes = num_classes
        self.mask_train_u = mask_train_u
        self.mask_train_l = mask_train_l
        self.mask_val = mask_val
        self.mask_test = mask_test

    def add_to_train_labeled_indices(self, indices: Int[Tensor, " num_acquired"]):
        """Adds new indices to training indices."""
        assert not (self.mask_train_l[indices]).any(), "Some of the indices that are to be added were already acquired"
        assert (self.mask_train_u[indices]).all(), "Some of the indices that are to be added were not in the train pool"
        self.mask_train_u[indices] = False
        self.mask_train_l[indices] = True

    @property
    def node_degrees_in(self) -> Int[Tensor, " num_nodes"]:
        return torch_scatter.scatter_add(
            torch.ones(self.edge_index.size(1), device=self.edge_index.device),
            self.edge_index[1],
        )

    @property
    def node_degrees_out(self) -> Int[Tensor, " num_nodes"]:
        return torch_scatter.scatter_add(
            torch.ones(self.edge_index.size(1), device=self.edge_index.device),
            self.edge_index[0],
        )

    @property
    def num_train(self) -> int:
        return int(self.mask_train_u.sum().item() + self.mask_train_l.sum().item())

    @property
    def num_val(self) -> int:
        return int(self.mask_val.sum().item())

    @property
    def num_test(self) -> int:
        return int(self.mask_test.sum().item())

    @property
    def num_train_labeled(self) -> int:
        return int(self.mask_train_l.sum().item())

    @property
    def class_counts(self) -> Int[Tensor, " num_classes"]:
        return torch_scatter.scatter_add(torch.ones_like(self.y), self.y, dim_size=self.num_classes)

    @property
    def class_counts_train(self) -> Int[Tensor, " num_classes"]:
        y = self.y[self.mask_train_u | self.mask_train_l]
        return torch_scatter.scatter_add(torch.ones_like(y), y, dim_size=self.num_classes)

    @property
    def class_prior_probabilities_train(self) -> Float[Tensor, " num_classes"]:
        counts = self.class_counts_train
        if counts.sum() == 0:
            counts = torch.ones(self.num_classes, device=counts.device, dtype=torch.float)
        else:
            counts = counts.float()
        return counts / (counts.sum() + 1e-12)

    @property
    def masks_valid(self) -> bool:
        """Whether the masks are valid

        Returns
        -------
        bool : if masks are valid
        """
        if (
            not (
                (
                    self.get_mask(DatasetSplit.TRAIN_U).long()
                    + self.get_mask(DatasetSplit.TRAIN_L).long()
                    + self.get_mask(DatasetSplit.VAL).long()
                    + self.get_mask(DatasetSplit.TEST).long()
                )
                == 1
            )
            .all()
            .item()
        ):
            logger.error("Masks are not valid: some nodes are in multiple splits or no split at all")
            return False
        return True

    def print_masks(self):
        """For debugging: Print ratios of the masks."""
        logger.debug("Dataset mask ratio")
        for split in DatasetSplit:
            logger.debug(f"{split}: {self.get_mask(split).float().mean().item()}")

    def get_mask(self, which: DatasetSplit) -> Bool[Tensor, " num_nodes"]:
        match which:
            case DatasetSplit.TRAIN_L:
                return self.mask_train_l
            case DatasetSplit.TRAIN_U:
                return self.mask_train_u
            case DatasetSplit.TRAIN_ALL:
                return self.mask_train_l | self.mask_train_u
            case DatasetSplit.VAL:
                return self.mask_val
            case DatasetSplit.TEST:
                return self.mask_test
            case DatasetSplit.ALL:
                return torch.ones_like(self.mask_train_l, dtype=torch.bool)
            case _:
                raise ValueError(which)

    def get_diffused_node_features(self, k: int, normalize: bool, improved: bool, add_self_loops: bool, cache: bool):
        """Gets (and caches) nodes features after GCN convolutions"""
        key = f"diffused_node_features_{k}_{normalize}_{improved}_{add_self_loops}"

        diffused = getattr(self, key, None) if cache else None
        if diffused is not None:
            return diffused  # type: ignore
        # Compute the diffused node features

        edge_index, edge_weight = self.edge_index, getattr(self, "edge_weight", None)
        x = self.x
        if normalize:
            edge_index, edge_weight = tgnn.conv.gcn_conv.gcn_norm(  # yapf: disable
                edge_index, edge_weight, x.size(0), improved=improved, add_self_loops=add_self_loops
            )
        elif edge_weight is None:
            edge_weight = torch.ones(edge_index.size(1), device=edge_index.device)

        src, dst = edge_index
        for _ in range(k):
            # Perform message passing
            messages = x[src] * edge_weight[:, None]  # type: ignore
            x = torch_scatter.scatter_add(messages, dst, dim=0, dim_size=x.size(0))
        if cache:
            setattr(self, key, x)
        return x


class ActiveLearningDataset(TorchDataset):
    """A wrapper around base datasets that is responsible for splitting. It also keeps
    track of the state of the sampled nodes."""

    def __init__(self, config: DatasetConfig, base: GraphDataset):
        self.base = base
        self.val_size = config.common.val_size

        # Setup the test mask
        if self.base.mask_test is not None:
            mask_test = self.base.mask_test
        elif config.common.test_size == 0:
            mask_test = torch.zeros(self.base.num_nodes, dtype=torch.bool)
        else:
            rng_test = torch.Generator()
            rng_test.manual_seed(
                0x8D2CBCFC3A
            )  # A random test seed to keep test splits fixed among different calls of `self.split`
            mask_test = torch.zeros(self.base.num_nodes, dtype=torch.bool)
            for y in range(self.base.num_classes):
                mask_test |= sample_from_mask(self.base.labels == y, config.common.test_size, generator=rng_test)

        # The base data instance is directly derived from `self.base` and serves as a "template"
        self.base_data = self.transform(
            GraphData(
                x=self.base.node_features,
                y=self.base.labels,
                edge_index=self.base.edge_indices,
                mask_test=mask_test,
                num_classes=self.base.num_classes,
            )
        )
        self.data: GraphData = self.base_data.clone()

    def print_masks(self):
        self.data.print_masks()

    def transform(self, data: GraphData) -> GraphData:
        # do nothing
        return data

    @property
    def masks_valid(self) -> bool:
        return self.data.masks_valid

    def reset_train_idxs(self):
        """Resets the train idxs to the empty set and the train pool to the remaining indices."""
        self.data.mask_train_l = torch.zeros_like(self.data.mask_test)
        self.data.mask_train_u = ~(self.data.mask_test | self.data.mask_val)
        assert self.masks_valid

    def split(
        self,
        generator: torch.Generator | None = None,
    ) -> Self:
        """Resets the training mask and applies a new dataset split if the dataset permits it.

        Parameters
        ----------
        generator : torch.Generator | None
            A generator for getting the split
        """
        if self.base.mask_val is not None:
            mask_val = self.base.mask_val.to(self.data.mask_test.device)
        elif self.val_size == 0:
            mask_val = torch.zeros_like(self.data.mask_train_u)
        else:
            mask_val = torch.zeros_like(self.data.mask_train_u, dtype=torch.bool)
            for y in range(self.base.num_classes):
                if isinstance(self.val_size, float):
                    val_size = int((self.data.y == y).sum().item() * self.val_size)
                elif isinstance(self.val_size, int):
                    val_size = self.val_size
                else:
                    raise ValueError(f"Validation set size must be int or float, but got {type(self.val_size)}")

                mask_val_pool = (self.data.y == y) & (~self.data.mask_test)
                mask_val |= sample_from_mask(mask_val_pool, val_size, generator=generator)
        self.data.mask_val = mask_val

        self.reset_train_idxs()
        return self

    def select_initial_pool(self, type_: InitialPoolSelectionType, rng: torch.Generator) -> Self:
        """select initial pool"""
        match type_:
            case InitialPoolSelectionType.BALANCED:
                index_pool = []
                for y in range(self.base.num_classes):
                    for _ in range(1):  # select one sample per class
                        mask_pool = (self.data.y == y) & (self.data.mask_train_u)
                        selected_idx = sample_from_mask(mask=mask_pool, size=1, generator=rng).nonzero().item()
                        self.add_to_train_labeled_indices(indices=[selected_idx])
                        index_pool.append(selected_idx)
                logger.info("initial pool: %s", index_pool)
                return self
            case InitialPoolSelectionType.RANDOM:
                selected_idx = sample_from_mask(mask=self.data.mask_train_u, size=1*self.base.num_classes, generator=rng).nonzero().view(-1)
                self.add_to_train_labeled_indices(indices=selected_idx)
                logger.info("initial pool: %s", selected_idx.tolist())
                return self
            case InitialPoolSelectionType.RANDOM_1:
                selected_idx = sample_from_mask(mask=self.data.mask_train_u, size=1, generator=rng).nonzero().view(-1)
                self.add_to_train_labeled_indices(indices=selected_idx)
                logger.info("initial pool: %s", selected_idx.tolist())
                return self

    def cuda(self) -> Self:
        self.data = self.data.cuda()
        return self

    def cpu(self) -> Self:
        self.data = self.data.cpu()
        return self

    def add_to_train_labeled_indices(self, indices: Int[Tensor, " num_acquired"]):
        """Adds new indices to training indices."""
        self.data.add_to_train_labeled_indices(indices)

    def __getitem__(self, idx: int) -> GraphData:
        if idx >= len(self):
            raise IndexError(f"Trying to index {self} of size {len(self)} with index {idx}")
        return self.data

    def __len__(self) -> int:
        return 1

    @property
    def num_nodes(self) -> int:
        assert self.data.num_nodes is not None, "GraphData object has no nodes"
        return self.data.num_nodes

    @property
    def num_edges(self) -> int:
        return self.data.num_edges

    @property
    def num_input_features(self) -> int:
        return self.data.num_node_features

    @property
    def num_train_nodes(self) -> int:
        return self.data.num_train

    @property
    def num_val_nodes(self) -> int:
        return self.data.num_val

    @property
    def num_test_nodes(self) -> int:
        return self.data.num_test

    @property
    def num_train_labeled_nodes(self) -> int:
        return self.data.num_train_labeled

    @property
    def num_classes(self) -> int:
        return int(self.data.num_classes)

    @property
    def node_degrees_in(self) -> Int[Tensor, " num_nodes"]:
        return self.data.node_degrees_in

    @property
    def node_degrees_out(self) -> Int[Tensor, " num_nodes"]:
        return self.data.node_degrees_out


def sample_from_mask(
    mask: Bool[Tensor, " num_nodes"],
    size: int | float,
    generator: torch.Generator | None = None,
) -> Bool[Tensor, " num_nodes"]:
    """Samples indices from a mask of possible indices.

    Parameters
    ----------
    mask : Bool[Tensor, "num_nodes"])
        All available indices
    size : int | float
        How many (absolute or as a fraction) to sample
    generator : torch.Generator | None
        A random number generator for sampling

    Returns
    -------
    Bool[Tensor, "num_nodes"] : Sampled indices
    """
    mask_size = mask.sum().item()

    result = torch.zeros_like(mask)
    if isinstance(size, float):
        size = int(size * mask_size)
    elif not isinstance(size, int):
        raise ValueError(f"Size to sample must either be int or float, but got {type(size)}")
    if size == 0:
        logger.warning(f"Sampling {size} (type {type(size)}) from a mask of size {mask_size}")
        return result
    elif size > mask_size:
        raise RuntimeError(f"Trying to sample {size} indices from a mask containing {mask_size} elements")
    else:
        indices = torch.where(mask)[0]
        indices = indices[torch.randperm(indices.size(0), generator=generator)[:size]]
        result[indices] = True
        return result
