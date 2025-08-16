from dataclasses import dataclass, field
from pathlib import Path

from cp4bal.util.enums import EdgeProbabilityType, ModelName, TrainerType
from cp4bal.util.paths import get_root_path


# Dataset
@dataclass
class CommonDatasetConfig:
    seed: int | None = None

    name: str | None = None

    num_nodes: int = 140
    num_classes: int | None = None
    dim_features: int | None = None

    val_size: float = 0.2  # How many nodes to use as validation
    test_size: float = 0.2  # How many nodes to use as test


@dataclass
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


@dataclass
class DatasetConfig:
    common: CommonDatasetConfig
    detail: CSBMConfig | None = None


# Model
@dataclass
class ModelConfig:
    name: ModelName | None = None


@dataclass
class MultipleSampleModelConfig(ModelConfig):
    """Configuration to support drawing from multiple samples."""

    num_samples_train: int = 1
    num_samples_eval: int = 1


@dataclass
class MCDropoutModelConfig(MultipleSampleModelConfig):
    """Configuration for models that sample using MC dropout."""

    dropout_at_eval: bool = False
    dropout_p: float = 0.0


@dataclass
class GCNConfig:
    name: ModelName = ModelName.GCN
    hidden_dims: list[int] = field(
        default_factory=lambda: (
            32,
            32,
        )
    )
    add_self_loops: bool = True
    cached = True
    improved = False  # If True, sets self-weight to 2
    inplace: bool = True  # If True, uses inplace ReLU


# Trainer
@dataclass
class TrainerConfig:
    """Base trainer configuration."""

    name: TrainerType
    reset_parameter_before_training: bool = True
    progress_bar: bool = False  # Progress bar for training a single model
    use_gpu: bool = True
    verbose: bool = False


@dataclass
class EarlyStoppingConfig:
    """Early stopping configuration."""

    higher_is_better: bool = False
    patience: int = 10
    min_delta: float = 1e-3  # Improvement of less than this value will be discarded
    save_model_state: bool = False


class OracleTrainerConfig(TrainerConfig):
    """Configuration for the OracleTrainer."""

    name: TrainerType = TrainerType.ORACLE


class SGDTrainerConfig(TrainerConfig):
    """Configuration for the SGDTrainer."""

    name: TrainerType = TrainerType.SGD

    max_epochs: int = 10000
    min_epochs: int = 0

    logits_propagated: bool = True
    early_stopping: EarlyStoppingConfig | None = None


# Interface
@dataclass
class SystemConfig:
    """Configuration for the system."""

    root: Path = get_root_path()
    artifact_dir: Path = root / "artifact"
    log_dir: Path = root / "log"
    out_dir: Path = root / "out"
    seed: int = 42
    device: str = "cpu"
    num_workers: int = 4


@dataclass
class ExperimentConfig:
    """Configuration for the experiment."""

    name: str = "auto"


@dataclass
class ActiveLearningConfig:
    """
    Configuration for active learning experiments.
    """

    acquisition_type: str = "random"
    num_rounds: int = 10
    budget_per_round: int | None = None
    num_epochs: int = 100
    trainer_type: str = "oracle"


@dataclass
class OverallConfig:
    """Configuration for the overall experiment."""

    system: SystemConfig
    experiment: ExperimentConfig
    al: ActiveLearningConfig
    data: DatasetConfig
    model: ModelConfig

    def __post_init__(self):
        self.unique_name = f"{self.data.common.name}/{self.experiment.name}"
        self.system.artifact_dir.mkdir(parents=True, exist_ok=True)
        self.system.log_dir.mkdir(parents=True, exist_ok=True)
        (self.system.out_dir / self.unique_name).mkdir(parents=True, exist_ok=True)


@dataclass
class ArgConfig:
    """Configuration for the argument parser."""

    seed: int
    gpu_id: int
    experiment_name: str
    model_config: Path
    al_config: Path
    dataset_config: Path
