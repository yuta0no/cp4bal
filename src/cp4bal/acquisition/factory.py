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
    FeatureCoresetAcquisitionConfig,
    GraphCoresetAcquisitionConfig,
    LeastConfidenceAcquisitionConfig,
    MarginAcquisitionConfig,
    OracleUncertaintyAcquisitionConfig,
    OracleUncertaintyWithConfidencePropagationAcquisitionConfig,
    RandomAcquisitionConfig,
)
from .coreset import CoresetAcquisition
from .degree import DegreeAcquisition
from .energy import EnergyAcquisition
from .entropy import EntropyAcquisition
from .enums import AcquisitionType
from .least_confidence import LeastConfidenceAcquisition
from .margin import MarginAcquisition
from .oracle_uncertainty import OracleUncertaintyAcquisition
from .oracle_uncertainty_cp import OracleUncertaintyWithConfidencePropagationAcquisition
from .random import RandomAcquisition


class AcquisitionFactory:
    @staticmethod
    def create(config: AcquisitionConfig) -> Acquisition:
        match config.type_:
            case AcquisitionType.CORESET_FEATURE:
                if not isinstance(config, FeatureCoresetAcquisitionConfig):
                    raise ValueError(f"Invalid config for coreset acquisition: {config}")
                return CoresetAcquisition(config=config)
            case AcquisitionType.CORESET_GRAPH:
                if not isinstance(config, GraphCoresetAcquisitionConfig):
                    raise ValueError(f"Invalid config for coreset acquisition: {config}")
                return CoresetAcquisition(config=config)
            case AcquisitionType.DEGREE:
                if not isinstance(config, DegreeAcquisitionConfig):
                    raise ValueError(f"Invalid config for degree acquisition: {config}")
                return DegreeAcquisition(config=config)
            case AcquisitionType.ENERGY:
                if not isinstance(config, EnergyAcquisitionConfig):
                    raise ValueError(f"Invalid config for energy acquisition: {config}")
                return EnergyAcquisition(config=config)
            case AcquisitionType.ENTROPY:
                if not isinstance(config, EntropyAcquisitionConfig):
                    raise ValueError(f"Invalid config for entropy acquisition: {config}")
                return EntropyAcquisition(config=config)
            case AcquisitionType.RANDOM:
                if not isinstance(config, RandomAcquisitionConfig):
                    raise ValueError(f"Invalid config for random acquisition: {config}")
                return RandomAcquisition(config=config)
            case AcquisitionType.LEAST_CONFIDENCE:
                if not isinstance(config, LeastConfidenceAcquisitionConfig):
                    raise ValueError(f"Invalid config for least confidence acquisition: {config}")
                return LeastConfidenceAcquisition(config=config)
            case AcquisitionType.MARGIN:
                if not isinstance(config, MarginAcquisitionConfig):
                    raise ValueError(f"Invalid config for margin acquisition: {config}")
                return MarginAcquisition(config=config)
            case AcquisitionType.ORACLE_UNCERTAINTY:
                if not isinstance(config, OracleUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for oracle uncertainty acquisition: {config}")
                return OracleUncertaintyAcquisition(config=config)
            case AcquisitionType.ORACLE_UNCERTAINTY_CP:
                if not isinstance(config, OracleUncertaintyWithConfidencePropagationAcquisitionConfig):
                    raise ValueError(f"Invalid config for oracle uncertainty_cp acquisition: {config}")
                return OracleUncertaintyWithConfidencePropagationAcquisition(config=config)
            case AcquisitionType.APPROXIMATE_UNCERTAINTY:
                if not isinstance(config, ApproximateUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for approximate uncertainty acquisition: {config}")
                return ApproximateUncertaintyAcquisition(config=config)
            case AcquisitionType.APPROXIMATE_UNCERTAINTY_CP:
                if not isinstance(config, ApproximateUncertaintyWithConfidencePropagationAcquisitionConfig):
                    raise ValueError(f"Invalid config for approximate uncertainty acquisition: {config}")
                return ApproximateUncertaintyWithConfidencePropagationAcquisition(config=config)
            case _:
                raise ValueError(f"Unknown acquisition type: {config.type_.name}")
