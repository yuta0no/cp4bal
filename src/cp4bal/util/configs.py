from dataclasses import dataclass, field
from pathlib import Path

from cp4bal.util.enums import AcquisitionType, EdgeProbabilityType, ModelName, TrainerType, UncertaintyType
from cp4bal.util.paths import get_root_path


# Acquisition
@dataclass(kw_only=True)
class AcquisitionConfig:
    type_: AcquisitionType
    requires_model_predictions: bool = False


@dataclass(kw_only=True)
class RandomAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.RANDOM
    requires_model_predictions: bool = False


@dataclass(kw_only=True)
class EntropyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ENTROPY
    requires_model_predictions: bool = True


@dataclass(kw_only=True)
class OracleUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ORACLE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC


# Dataset
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


# Model
@dataclass(kw_only=True)
class ModelConfig:
    name: ModelName | None = None


@dataclass(kw_only=True)
class MultipleSampleModelConfig(ModelConfig):
    """Configuration to support drawing from multiple samples."""

    num_samples_train: int = 1
    num_samples_eval: int = 1


@dataclass(kw_only=True)
class MCDropoutModelConfig(MultipleSampleModelConfig):
    """Configuration for models that sample using MC dropout."""

    dropout_at_eval: bool = False
    dropout_p: float = 0.0


@dataclass(kw_only=True)
class GCNConfig(MCDropoutModelConfig):
    name: ModelName = ModelName.GCN
    hidden_dims: list[int] = field(default_factory=lambda: (32,))
    add_self_loops: bool = True
    cached = True
    improved = False  # If True, sets self-weight to 2
    inplace: bool = True  # If True, uses inplace ReLU


# Trainer
@dataclass(kw_only=True)
class TrainerConfig:
    """Base trainer configuration."""

    name: TrainerType
    reset_parameter_before_training: bool = True
    progress_bar: bool = False  # Progress bar for training a single model
    use_gpu: bool = True
    verbose: bool = False


@dataclass(kw_only=True)
class EarlyStoppingConfig:
    """Early stopping configuration."""

    higher_is_better: bool = False
    patience: int = 10
    min_delta: float = 1e-3  # Improvement of less than this value will be discarded
    save_model_state: bool = False


@dataclass(kw_only=True)
class OracleTrainerConfig(TrainerConfig):
    """Configuration for the OracleTrainer."""

    name: TrainerType = TrainerType.ORACLE


@dataclass(kw_only=True)
class AdamTrainerConfig(TrainerConfig):
    """Configuration for the AdamTrainer."""

    name: TrainerType = TrainerType.ADAM

    lr: float = 0.001
    weight_decay: float = 0.0

    max_epochs: int = 100
    min_epochs: int = 0

    logits_propagated: bool = True
    early_stopping: EarlyStoppingConfig | None = None


# Interface
@dataclass(kw_only=True)
class SystemConfig:
    """Configuration for the system."""

    root: Path = get_root_path()
    artifact_dir: Path = root / "artifact"
    log_dir: Path = root / "log"
    out_dir: Path = root / "out"
    seed: int = 42
    device: str = "cpu"
    num_workers: int = 4


@dataclass(kw_only=True)
class ExperimentConfig:
    """Configuration for the experiment."""

    name: str = "auto"


@dataclass(kw_only=True)
class ActiveLearningConfig:
    """
    Configuration for active learning experiments.
    """

    acquisition_type: str = "random"
    num_rounds: int = 10
    budget_per_round: int | None = None
    num_epochs: int = 100
    trainer_type: str = "oracle"


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ArgConfig:
    """Configuration for the argument parser."""

    seed: int
    gpu_id: int
    experiment_name: str
    model_config: Path
    al_config: Path
    dataset_config: Path
