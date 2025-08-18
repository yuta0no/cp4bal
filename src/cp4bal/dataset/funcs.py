from logging import getLogger
from typing import Tuple

import numpy as np
from jaxtyping import Int

from .enums import ImplementationType

logger = getLogger(__name__)

impl_type = ImplementationType.VANILLA


def count_in_class_by_triangular_upper_adjacency(
    labels: Int[np.ndarray, "num_assignments num_nodes"],
    edge_indices: Int[np.ndarray, "2 num_edges"],
    num_classes: int,
) -> Tuple[
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
]:
    """counts how often a label appears in the (non-)neighboring nodes of a node

    Parameters
    ----------
    labels : Int[np.ndarray, "num_assignments num_nodes"]
        Labels of the nodes
    edge_indices : Int[np.ndarray, "2 num_edges"]
        Edge indices of the graph
    num_classes : int
        Number of classes in the dataset

    Returns
    -------
    counts : Int[np.ndarray, 'num_assignments num_nodes num_classes']
        Counts of labels in the samples
    counts_in_neighbors : Int[np.ndarray, 'num_assignments num_nodes num_classes']
        Counts of labels in the neighboring nodes
    counts_in_non_neighbors : Int[np.ndarray, 'num_assignments num_nodes num_classes']
        Counts of labels in the non-neighboring nodes. Does not count self-loops as a non-neighbor.
    """
    match impl_type:
        # case ImplementationType.NUMBA:
        #     ret = count_in_class_by_triangular_upper_adjacency_numba(
        #         labels=labels,
        #         edge_indices=edge_indices,
        #         num_classes=num_classes,
        #     )
        case ImplementationType.VANILLA:
            ret = count_in_class_by_triangular_upper_adjacency_py(
                labels=labels,
                edge_indices=edge_indices,
                num_classes=num_classes,
            )
        case _:
            raise ValueError(f"Unknown implementation type: {impl_type}")
    # logger.info("end (tri count)")
    return ret


def class_counts_by_node_to_affiliation_counts(
    class_counts: Int[np.ndarray, "num_assignments num_nodes num_classes"],
    labels: Int[np.ndarray, "num_assignments num_nodes"],
) -> Int[np.ndarray, "num_assignments num_classes num_classes"]:
    """Transforms class counts per node to affiliation counts, i.e. counting how often a class links to a class.

    Parameters
    ----------
    class_counts : Int[np.ndarray, 'num_assignments num_nodes num_classes']
        For each node in each assignment, how often it counts a class
    labels : Int[np.ndarray, 'num_assignments num_nodes']
        For each `num_assignments` samples, what the node class assignments are (i.e. row corresponds to assignment)

    Returns
    -------
    affiliation_counts : Int[np.ndarray, 'num_assignments num_classes num_classes']
        For each assignment, how often classes are affilated
    """
    match impl_type:
        # case ImplementationType.NUMBA:
        #     return class_counts_by_node_to_affiliation_counts_numba(
        #         class_counts=class_counts, labels=labels
        #     )
        case ImplementationType.VANILLA:
            return class_counts_by_node_to_affiliation_counts_py(class_counts=class_counts, labels=labels)
        case _:
            raise ValueError(f"Unknown implementation type: {impl_type}")


def count_in_class_by_triangular_upper_adjacency_py(
    labels: Int[np.ndarray, "num_assignments num_nodes"],
    edge_indices: Int[np.ndarray, "2 num_edges"],
    num_classes: int,
) -> Tuple[
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
    Int[np.ndarray, "num_assignments num_nodes num_classes"],
]:
    """Python implementation of counting how often a label appears in the (non-)neighboring nodes of a node"""
    S = labels.shape[0]
    N = labels.shape[1]
    E = edge_indices.shape[1]
    counts = np.zeros([S, N, num_classes], dtype=int)
    counts_adj = np.zeros([S, N, num_classes], dtype=int)
    counts_non_adj = np.zeros([S, N, num_classes], dtype=int)

    # Per sample, count the number of nodes in each class per row of the upper triangular adjacency
    for s in range(S):
        for v in range(N):
            for u in range(v):  # all the rows for which v is counted (we only count the upper triangular part)
                counts[s, u, labels[s, v]] += 1

    # Per sample, per node, count the number adjacent nodes in each class
    for s in range(S):
        for e in range(E):
            counts_adj[s, edge_indices[0, e], labels[s, edge_indices[1, e]]] += 1

    # Compute the number of non-adjacent nodes as the difference of the above
    for s in range(S):
        for v in range(N):
            for c in range(num_classes):
                counts_non_adj[s, v, c] = counts[s, v, c] - counts_adj[s, v, c]

    return counts, counts_adj, counts_non_adj


def class_counts_by_node_to_affiliation_counts_py(
    class_counts: Int[np.ndarray, "num_assignments num_nodes num_classes"],
    labels: Int[np.ndarray, "num_assignments num_nodes"],
) -> Int[np.ndarray, "num_assignments num_classes num_classes"]:
    """Python implementation of transforming class counts per node to affiliation counts,
    i.e. counting how often a class links to a class."""
    S, N, C = class_counts.shape

    affiliation_counts = np.zeros([S, C, C], dtype=int)
    for s in range(S):
        for v in range(N):
            for c in range(C):
                affiliation_counts[s, labels[s, v], c] += class_counts[s, v, c]

    return affiliation_counts


# numba implementations
# @jit(nopython=True, cache=True)
# def _count_class_numba(
#     S: int, N: int, C: int, labels: Int[np.ndarray, "num_assignments num_nodes"]
# ) -> Int[np.ndarray, "num_assignments num_nodes num_classes"]:
#     counts = np.zeros((S, N, C), dtype=np.int64)
#     for s in range(S):
#         for v in range(N):
#             for u in range(v):
#                 counts[s, u, labels[s, v]] += 1
#     return counts.astype(np.int64)


# @jit(nopython=True, cache=True)
# def _count_adj_numba(
#     S: int,
#     E: int,
#     N: int,
#     C: int,
#     edge_indices: Int[np.ndarray, "2 num_edges"],
#     labels: Int[np.ndarray, "num_assignments num_nodes"],
# ) -> Int[np.ndarray, "num_assignments num_nodes num_classes"]:
#     counts_adj = np.zeros((S, N, C), dtype=np.int64)
#     for s in range(S):
#         for e in range(E):
#             counts_adj[s, edge_indices[0, e], labels[s, edge_indices[1, e]]] += 1
#     return counts_adj


# @jit(nopython=True, cache=True)
# def _count_non_adj_numba(
#     S: int,
#     N: int,
#     C: int,
#     counts: Int[np.ndarray, "num_assignments num_nodes num_classes"],
#     counts_adj: Int[np.ndarray, "num_assignments num_nodes num_classes"],
# ) -> Int[np.ndarray, "num_assignments num_nodes num_classes"]:
#     counts_non_adj = np.zeros((S, N, C), dtype=np.int64)
#     for s in range(S):
#         for v in range(N):
#             for c in range(C):
#                 counts_non_adj[s, v, c] = counts[s, v, c] - counts_adj[s, v, c]
#     return counts_non_adj


# @jit(nopython=True, cache=True)
# def count_in_class_by_triangular_upper_adjacency_numba(
#     labels: Int[np.ndarray, "num_assignments num_nodes"],
#     edge_indices: Int[np.ndarray, "2 num_edges"],
#     num_classes: int,
# ) -> Tuple[
#     Int[np.ndarray, "num_assignments num_nodes num_classes"],
#     Int[np.ndarray, "num_assignments num_nodes num_classes"],
#     Int[np.ndarray, "num_assignments num_nodes num_classes"],
# ]:
#     """Numba implementation of counting how often a label appears
#     in the (non-)neighboring nodes of a node"""
#     S = int(labels.shape[0])
#     N = int(labels.shape[1])
#     E = int(edge_indices.shape[1])
#     C = int(num_classes)
#     labels = labels.astype(np.int64)
#     edge_indices = edge_indices.astype(np.int64)
#     counts = _count_class_numba(S, N, C, labels)
#     counts_adj = _count_adj_numba(S, E, N, C, edge_indices, labels)
#     counts_non_adj = _count_non_adj_numba(S, N, C, counts, counts_adj)
#     return counts, counts_adj, counts_non_adj


# @jit(nopython=True, cache=True)
# def class_counts_by_node_to_affiliation_counts_numba(
#     class_counts: Int[np.ndarray, "num_assignments num_nodes num_classes"],
#     labels: Int[np.ndarray, "num_assignments num_nodes"],
# ) -> Int[np.ndarray, "num_assignments num_classes num_classes"]:
#     """Numba implementation of transforming class counts per node to affiliation counts,
#     i.e. counting how often a class links to a class."""
#     S, N, C = class_counts.shape
#     S = int(S)
#     N = int(N)
#     C = int(C)
#     affiliation_counts = np.zeros((S, C, C), dtype=np.int64)
#     for s in range(S):
#         for v in range(N):
#             for c in range(C):
#                 affiliation_counts[s, labels[s, v], c] += class_counts[s, v, c]

#     return affiliation_counts
