import uuid
from dataclasses import dataclass
from datetime import datetime
from math import ceil, log
from pathlib import Path
from typing import Self
from zoneinfo import ZoneInfo

import yaml

from cp4bal.acquisition.configs import (
    AcquisitionConfig,
    ApproximateUncertaintyAcquisitionConfig,
    OracleUncertaintyAcquisitionConfig,
    RandomAcquisitionConfig,
)
from cp4bal.dataset.configs import (
    CommonDatasetConfig,
    CSBMConfig,
    DatasetConfig,
    TorchGeometricDataConfig,
    TorchGeometricDatasetType,
)
from cp4bal.dataset.enums import EdgeProbabilityType
from cp4bal.model.configs import BayesOptimalConfig, GCNConfig, ModelConfig, SGCConfig
from cp4bal.model.trainer.configs import AdamTrainerConfig, OracleTrainerConfig, SGCTrainerConfig, TrainerConfig
from cp4bal.util.configs import ActiveLearningConfig, ExperimentConfig


@dataclass
class ConfigBuilderInterface:
    acquisition: AcquisitionConfig
    experiment: ExperimentConfig
    al: ActiveLearningConfig
    dataset: DatasetConfig
    trainer: TrainerConfig
    model: ModelConfig


@dataclass
class ConfigBuilderStates:
    # Common
    seed: int | None = None
    experiment_name: str | None = None
    # Dataset
    ds_name: str | None = None
    n_nodes: int | None = None
    n_classes: int | None = None
    dim_features: int | None = None
    val_size: float | None = None
    test_size: float | None = None
    # CSBM
    feature_sigma: float | None = None
    feature_class_mean_distance: float | None = None
    edge_p_type: EdgeProbabilityType | None = None
    expected_degree: int | None = None
    edge_p_snr: float | None = None
    # Acquisition
    acquisition_name: str | None = None
    propagation: bool | None = None
    # Active Learning
    budget: int | None = None
    round: int | None = None
    # Trainer
    trainer_name: str | None = None
    # Model
    model_name: str | None = None


class ConfigBuilder:
    def __init__(self):
        self._states = ConfigBuilderStates()

    def build(self) -> ConfigBuilderInterface:
        dataset_config = self._build_dataset_config()
        trainer_config = self._build_trainer_config()
        model_config = self._build_model_config(trainer_config=trainer_config)
        acquisition_config = self._build_acquisition_config()
        al_config = ActiveLearningConfig(
            budget_per_round=self._states.budget,
            num_rounds=self._states.round,
        )
        experiment_config = self._build_experiment_config(
            model_config=model_config,
            ds_config=dataset_config,
            acquisition_config=acquisition_config,
            al_config=al_config,
        )
        return ConfigBuilderInterface(
            acquisition=acquisition_config,
            dataset=dataset_config,
            experiment=experiment_config,
            trainer=trainer_config,
            model=model_config,
            al=al_config,
        )

    def _build_dataset_config(self) -> DatasetConfig:
        if self._states.ds_name.lower().startswith("csbm"):
            dc = CSBMConfig(
                seed=self._states.seed,
                num_nodes=self._states.n_nodes,
                num_classes=self._states.n_classes,
                dim_features=self._states.dim_features,
                feature_sigma=self._states.feature_sigma,
                feature_class_mean_distance=self._states.feature_class_mean_distance,
                edge_p_type=self._states.edge_p_type,
                p_edge_inter=None,
                p_edge_intra=None,
                expected_degree=self._states.expected_degree,
                edge_p_snr=self._states.edge_p_snr,
            )
        elif self._states.ds_name.lower() in [d.value for d in TorchGeometricDatasetType]:
            type_ = TorchGeometricDatasetType(self._states.ds_name.lower())
            dc = TorchGeometricDataConfig(torch_geometric_dataset=type_)
        else:
            raise ValueError(f"Unknown dataset name: {self._states.ds_name}")
        return DatasetConfig(
            common=CommonDatasetConfig(
                name=self._states.ds_name,
                val_size=self._states.val_size,
                test_size=self._states.test_size,
            ),
            detail=dc,
        )

    def _build_model_config(self, trainer_config: TrainerConfig) -> ModelConfig:
        if self._states.model_name is None:
            raise ValueError("Model name must be set before building the config.")
        match self._states.model_name.lower():
            case "gcn":
                return GCNConfig(trainer=trainer_config)
            case "sgc":
                return SGCConfig(trainer=trainer_config)
            case "bayes_optimal":
                return BayesOptimalConfig(trainer=trainer_config)
            case _:
                raise ValueError(f"Model {self._states.model_name} is not supported.")

    def _build_trainer_config(self) -> TrainerConfig:
        if self._states.trainer_name is None:
            raise ValueError("Trainer name must be set before building the config.")
        match self._states.trainer_name.lower():
            case "adam":
                return AdamTrainerConfig()
            case "sgc":
                return SGCTrainerConfig()
            case "oracle":
                return OracleTrainerConfig()
            case _:
                raise ValueError(f"Trainer {self._states.trainer_name} is not supported.")

    def _build_acquisition_config(self):
        if self._states.acquisition_name is None:
            raise ValueError("Acquisition name must be set before building the config.")
        if self._states.budget is None or self._states.budget <= 0:
            raise ValueError("Budget must be set and positive before building the config.")

        match self._states.acquisition_name.lower():
            case "random":
                return RandomAcquisitionConfig()
            case "oracle_uncertainty":
                return OracleUncertaintyAcquisitionConfig(
                    confidence_propagation=self._states.propagation,
                )
            case "approximate_uncertainty":
                return ApproximateUncertaintyAcquisitionConfig(
                    confidence_propagation=self._states.propagation,
                )

    def _build_experiment_config(
        self,
        ds_config: DatasetConfig,
        model_config: ModelConfig,
        acquisition_config: AcquisitionConfig,
        al_config: ActiveLearningConfig,
    ) -> ExperimentConfig:
        if self._states.experiment_name is None:
            raise ValueError("Experiment name must be set before building the config.")
        if self._states.experiment_name == "":
            raise ValueError("Experiment name cannot be an empty string.")
        if self._states.experiment_name == "auto":
            unique_key = uuid.uuid4().hex[:4]
            now = datetime.now(tz=ZoneInfo("Asia/Tokyo"))
            timestamp = now.strftime("%Y-%m-%dT%H:%M:%S")
            self._states.experiment_name = f"{ds_config.common.name}/{model_config.name}/{al_config.budget_per_round}"
            self._states.experiment_name += f"/{acquisition_config.type_.name.lower()}"
            if self._states.propagation and "uncertainty" in acquisition_config.type_.name.lower():
                self._states.experiment_name += "_cp"
            self._states.experiment_name += f"/{timestamp}-{unique_key}"
        return ExperimentConfig(
            name=self._states.experiment_name,
        )

    def load_dataset_config_file(self, file_path: Path) -> Self:
        with open(file_path, "r") as f:
            config: dict = yaml.safe_load(f)
        self.set_ds_name(config.get("name", self._states.ds_name))
        self.set_n_classes(config.get("num_classes", self._states.n_classes))
        self.set_val_size(config.get("val_size", self._states.val_size))
        self.set_test_size(config.get("test_size", self._states.test_size))
        if self._states.ds_name.startswith("csbm"):
            (
                self.set_csbm_n_nodes(config.get("n_nodes", self._states.n_nodes))
                .set_csbm_feature_sigma(config.get("feature_sigma", self._states.feature_sigma))
                .set_csbm_feature_class_mean_distance(
                    config.get("feature_class_mean_distance", self._states.feature_class_mean_distance)
                )
                .set_csbm_edge_p_type(config.get("edge_p_type", self._states.edge_p_type))
                .set_csbm_expected_degree(config.get("expected_degree", self._states.expected_degree))
                .set_csbm_edge_p_snr(config.get("edge_p_snr", self._states.edge_p_snr))
                .compute_csbm_dim_features()
            )
        return self

    def load_model_config_file(self, file_path: Path) -> Self:
        with open(file_path, "r") as f:
            config: dict = yaml.safe_load(f)
        self.set_model_name(config.get("model", self._states.model_name))
        self.set_trainer_name(config.get("trainer", self._states.trainer_name))
        return self

    # setters for dataset configs
    def set_ds_name(self, name: str) -> Self:
        self._states.ds_name = name
        return self

    def set_n_classes(self, n: int) -> Self:
        self._states.n_classes = n
        return self

    def set_val_size(self, size: float) -> Self:
        self._states.val_size = size
        return self

    def set_csbm_n_nodes(self, n: int) -> Self:
        self._states.n_nodes = n
        return self

    def compute_csbm_dim_features(self) -> Self:
        self._states.dim_features = max(
            self._states.n_classes, ceil(self._states.n_nodes / (log(self._states.n_nodes) * log(self._states.n_nodes)))
        )
        return self

    def set_test_size(self, size: float) -> Self:
        self._states.test_size = size
        return self

    def set_csbm_feature_sigma(self, sigma: float) -> Self:
        self._states.feature_sigma = sigma
        return self

    def set_csbm_feature_class_mean_distance(self, distance: float) -> Self:
        self._states.feature_class_mean_distance = distance
        return self

    def set_csbm_edge_p_type(self, edge_p_type: EdgeProbabilityType) -> Self:
        self._states.edge_p_type = edge_p_type
        return self

    def set_csbm_expected_degree(self, degree: int) -> Self:
        self._states.expected_degree = degree
        return self

    def set_csbm_edge_p_snr(self, snr: float) -> Self:
        self._states.edge_p_snr = snr
        return self

    # setters for acquisition configs
    def set_acquisition_name(self, name: str) -> Self:
        self._states.acquisition_name = name
        return self

    def set_propagation(self, propagation: bool) -> Self:
        self._states.propagation = propagation
        return self

    def set_budget(self, b: int) -> Self:
        self._states.budget = b
        return self

    def set_round(self, r: int) -> Self:
        self._states.round = r
        return self

    # setters for model and trainer configs
    def set_model_name(self, name: str) -> Self:
        self._states.model_name = name
        return self

    def set_trainer_name(self, name: str) -> Self:
        self._states.trainer_name = name
        return self

    # setters for common configs
    def set_seed(self, seed: int) -> Self:
        self._states.seed = seed
        return self

    def set_experiment_name(self, name: str) -> Self:
        self._states.experiment_name = name
        return self
