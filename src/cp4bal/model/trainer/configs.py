from dataclasses import dataclass

from .enums import TrainerType


@dataclass(kw_only=True)
class TrainerConfig:
    """Base trainer configuration."""

    name: TrainerType = TrainerType.MISSING
    reset_parameter_before_training: bool = True
    progress_bar: bool = False  # Progress bar for training a single model
    use_gpu: bool = True
    verbose: bool = False


@dataclass(kw_only=True)
class SGCTrainerConfig(TrainerConfig):
    """Configuration for the SGCTrainer."""

    name: TrainerType = TrainerType.SGC


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
