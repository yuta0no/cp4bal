from .approximate_uncertainty import ApproximateUncertaintyAcquisition
from .base import Acquisition
from .configs import (
    AcquisitionConfig,
    ApproximateUncertaintyAcquisitionConfig,
    OracleUncertaintyAcquisitionConfig,
    RandomAcquisitionConfig,
)
from .oracle_uncertainty import OracleUncertaintyAcquisition
from .random import RandomAcquisition


class AcquisitionFactory:
    @staticmethod
    def create(config: AcquisitionConfig) -> Acquisition:
        match config.type_.name.lower():
            case "random":
                if not isinstance(config, RandomAcquisitionConfig):
                    raise ValueError(f"Invalid config for random acquisition: {config}")
                return RandomAcquisition(config=config)
            case "oracle_uncertainty":
                if not isinstance(config, OracleUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for oracle uncertainty acquisition: {config}")
                return OracleUncertaintyAcquisition(config=config)
            case "approximate_uncertainty":
                if not isinstance(config, ApproximateUncertaintyAcquisitionConfig):
                    raise ValueError(f"Invalid config for approximate uncertainty acquisition: {config}")
                return ApproximateUncertaintyAcquisition(config=config)
            case _:
                raise ValueError(f"Unknown acquisition type: {config.type_.name}")
