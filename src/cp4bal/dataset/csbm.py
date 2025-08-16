from logging import getLogger

import networkx as nx
import numpy as np
import torch
from jaxtyping import Float
from scipy.stats import special_ortho_group
from torch import Tensor

from cp4bal.dataset import GraphDataset
from cp4bal.util.configs import CommonDatasetConfig, CSBMConfig
from cp4bal.util.enums import EdgeProbabilityType

logger = getLogger(__name__)


class CSBM(GraphDataset):
    def __init__(
        self,
        common_config: CommonDatasetConfig,
        csbm_config: CSBMConfig,
    ):
        rg = torch.Generator()

        num_classes = common_config.num_classes
        num_nodes = common_config.num_nodes
        dim_features = common_config.dim_features

        feature_sigma = csbm_config.feature_sigma

        # sample labels ~ p(y) and graph structure ~ p(A | y)
        p_edge_intra, p_edge_inter = self.__compute_edge_probabilities(
            type_=EdgeProbabilityType.BY_SNR_AND_DEGREE,
            num_classes=num_classes,
            num_nodes=num_nodes,
            expected_degree=csbm_config.expected_degree,
            edge_p_snr=csbm_config.edge_p_snr,
        )
        affiliation_matrix: Float[np.ndarray, "n_classes n_nodes"] = np.full(
            (num_classes, num_classes),
            p_edge_inter,
            dtype=float,
        )  # fill with q
        np.fill_diagonal(affiliation_matrix, p_edge_intra)  # diagonal to p
        nx_seed = int(torch.randint(2**16, size=(1,), generator=rg, dtype=torch.int).item())
        graph = nx.stochastic_block_model(
            sizes=[int(num_nodes / num_classes)] * num_classes,
            p=affiliation_matrix,
            seed=nx_seed,
            directed=False,
        )

        # labels to list
        ys = torch.ones((num_nodes,), dtype=torch.int) * -1
        for c, indices in enumerate(graph.graph["partition"]):
            ys[list(indices)] = c

        logger.info(f"labels are {ys.tolist()}")
        assert (ys >= 0).all()
        if len(graph.edges) == 0:
            logger.warning("Graph does not have any edges.")
            edge_indices = torch.tensor([], dtype=torch.int).resize(2, 0)
        else:
            edge_indices = torch.tensor(list(graph.edges)).T.contiguous()

        edge_indices = torch.cat((edge_indices, edge_indices.flip(0)), dim=-1)

        # sample node features ~ p(x | y)
        class_means = self._sample_class_means(torch_rng=rg, num_classes=num_classes, dim_features=dim_features)
        node_features = class_means[ys]
        node_features += torch.randn_like(node_features) * feature_sigma  # add noise

        # register instance variables
        self.node_features = node_features
        self.labels = ys
        self.edge_indices = edge_indices
        self.num_classes = num_classes
        self.class_means = class_means
        self.affiliation_matrix = affiliation_matrix
        self.class_prior = torch.full(
            (num_classes,),
            1.0 / num_classes,
            dtype=torch.float,
        )

        super().__init__(
            node_features=node_features,
            labels=ys,
            edge_indices=edge_indices,
            num_classes=num_classes,
            mask_train=None,
            mask_val=None,
            mask_test=None,
        )

    def __compute_edge_probabilities(
        self, type_: EdgeProbabilityType, num_classes: int, num_nodes: int, expected_degree: int, edge_p_snr: float
    ) -> tuple[float, float]:
        eps = 1e-8
        match type_:
            case EdgeProbabilityType.BY_SNR_AND_DEGREE:
                edge_probability_inter = (
                    expected_degree * num_classes / (num_nodes - 1) / (edge_p_snr + num_classes - 1)
                )  # q
                if edge_probability_inter > 1.0:
                    logger.warning(
                        f"Inter-community connection probability q for {num_classes} classes "
                        f"and {num_nodes} nodes with an expected degree of {expected_degree} "
                        f"and an SNR of {edge_p_snr} calculated to {edge_probability_inter} > 1.0. "
                        "Setting to 1.0"
                    )
                    edge_probability_inter = 1.0
                edge_probability_intra = edge_probability_inter * edge_p_snr  # p
                if edge_probability_intra > 1.0:
                    logger.warning(
                        f"Intra-community connection probability p for {num_classes} classes "
                        f"and {num_nodes} nodes with an expected degree of {expected_degree} "
                        f"and an SNR of {edge_p_snr} and an inter-community connection "
                        f"probability of {edge_probability_inter} calculated to {edge_probability_intra} > 1.0. "
                        "Setting to 1.0"
                    )
                    edge_probability_intra = 1.0
                return min(1.0 - eps, max(eps, edge_probability_intra)), min(
                    1.0 - eps, max(eps, edge_probability_inter)
                )

            case _:
                raise ValueError(f"Unsupported edge probability type: {type_}")

    def _sample_class_means(
        self, torch_rng: torch.Generator, num_classes: int, dim_features: int
    ) -> Float[Tensor, "num_classes dim_features"]:
        """Samples class means for the features based on the configuration.

        Parameters
        ----------
        torch_rng : torch.Generator
            The random number generator to use for sampling.
        num_classes : int
            Number of classes in graph
        dim_features : int
            Dimensionality of the feature space.

        Returns
        -------
        Float[Tensor, "num_classes dim_features"]
            A tensor of shape (num_classes, dim_features) containing the sampled class means.
        """
        FEATURE_CLASS_MEAN_DISTANCE = 1.0

        if num_classes > dim_features:
            raise ValueError(
                f"Number of classes {num_classes} must be less than or equal to the feature dimension {dim_features}."
            )
        means = torch.zeros(num_classes, dim_features)
        means[torch.arange(num_classes), torch.arange(num_classes)] = FEATURE_CLASS_MEAN_DISTANCE / np.sqrt(2)
        # random rotation
        rotation = torch.from_numpy(
            special_ortho_group.rvs(
                dim_features,
                random_state=int(torch.randint(2**16, size=(1,), generator=torch_rng, dtype=torch.int).item()),
            )
        ).float()
        means = means @ rotation
        return means
