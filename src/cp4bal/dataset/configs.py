from dataclasses import dataclass

from .enums import EdgeProbabilityType


@dataclass(kw_only=True)
class CommonDatasetConfig:
    seed: int | None = None

    name: str | None = None

    num_nodes: int = 140
    num_classes: int | None = None
    dim_features: int | None = None

    val_size: float = 0.2  # How many nodes to use as validation
    test_size: float = 0.2  # How many nodes to use as test


@dataclass(kw_only=True)
class CSBMConfig:
    """
    Configuration for the CSBM dataset.
    """

    feature_sigma: float | None = None
    feature_class_mean_distance: float | None = None

    edge_p_type: EdgeProbabilityType = EdgeProbabilityType.BY_SNR_AND_DEGREE

    p_edge_inter: float | None = None
    p_edge_intra: float | None = None
    edge_p_snr: float | None = None  # p_inter / p_intra
    expected_degree: float | None = None


@dataclass(kw_only=True)
class DatasetConfig:
    common: CommonDatasetConfig
    detail: CSBMConfig | None = None
