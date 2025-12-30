from .approximate_uncertainty import ApproximateUncertaintyAcquisition
from .approximate_uncertainty_cp import ApproximateUncertaintyWithConfidencePropagationAcquisition
from .base import Acquisition
from .configs import (
    AcquisitionConfig,
    ApproximateUncertaintyAcquisitionConfig,
    ApproximateUncertaintyWithConfidencePropagationAcquisitionConfig,
    DegreeAcquisitionConfig,
    EnergyAcquisitionConfig,
    EntropyAcquisitionConfig,
    LeastConfidenceAcquisitionConfig,
    MarginAcquisitionConfig,
    OracleUncertaintyAcquisitionConfig,
    OracleUncertaintyWithConfidencePropagationAcquisitionConfig,
    RandomAcquisitionConfig,
)
from .degree import DegreeAcquisition
from .energy import EnergyAcquisition
from .entropy import EntropyAcquisition
from .least_confidence import LeastConfidenceAcquisition
from .margin import MarginAcquisition
from .oracle_uncertainty import OracleUncertaintyAcquisition
from .oracle_uncertainty_cp import OracleUncertaintyWithConfidencePropagationAcquisition
from .random import RandomAcquisition


class AcquisitionFactory:
    @staticmethod
    def create(config: AcquisitionConfig) -> Acquisition:
        match config.type_.name.lower():
            case "degree":
                if not isinstance(config, DegreeAcquisitionConfig):
                    raise ValueError(f"Invalid config for degree acquisition: {config}")
                return DegreeAcquisition(config=config)
            case "energy":
                if not isinstance(config, EnergyAcquisitionConfig):
                    raise ValueError(f"Invalid config for energy acquisition: {config}")
                return EnergyAcquisition(config=config)
            case "entropy":
                if not isinstance(config, EntropyAcquisitionConfig):
                    raise ValueError(f"Invalid config for entropy acquisition: {config}")
                return EntropyAcquisition(config=config)
            case "random":
                if not isinstance(config, RandomAcquisitionConfig):
                    raise ValueError(f"Invalid config for random acquisition: {config}")
                return RandomAcquisition(config=config)
            case "least_confidence":
                if not isinstance(config, LeastConfidenceAcquisitionConfig):
                    raise ValueError(f"Invalid config for least confidence acquisition: {config}")
                return LeastConfidenceAcquisition(config=config)
            case "margin":
                if not isinstance(config, MarginAcquisitionConfig):
                    raise ValueError(f"Invalid config for margin acquisition: {config}")
                return MarginAcquisition(config=config)
            case "oracle_uncertainty":
                if not isinstance(config, OracleUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for oracle uncertainty acquisition: {config}")
                return OracleUncertaintyAcquisition(config=config)
            case "oracle_uncertainty_cp":
                if not isinstance(config, OracleUncertaintyWithConfidencePropagationAcquisitionConfig):
                    raise ValueError(f"Invalid config for oracle uncertainty_cp acquisition: {config}")
                return OracleUncertaintyWithConfidencePropagationAcquisition(config=config)
            case "approximate_uncertainty":
                if not isinstance(config, ApproximateUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for approximate uncertainty acquisition: {config}")
                return ApproximateUncertaintyAcquisition(config=config)
            case "approximate_uncertainty_cp":
                if not isinstance(config, ApproximateUncertaintyWithConfidencePropagationAcquisitionConfig):
                    raise ValueError(f"Invalid config for approximate uncertainty acquisition: {config}")
                return ApproximateUncertaintyWithConfidencePropagationAcquisition(config=config)
            case _:
                raise ValueError(f"Unknown acquisition type: {config.type_.name}")
