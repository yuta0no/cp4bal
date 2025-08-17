from dataclasses import dataclass
from pathlib import Path

from cp4bal.dataset.configs import DatasetConfig
from cp4bal.model.configs import ModelConfig
from cp4bal.util.paths import get_root_path


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
