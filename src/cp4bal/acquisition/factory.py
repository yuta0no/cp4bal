from .base import Acquisition
from .configs import OracleUncertaintyAcquisitionConfig
from .oracle_uncertainty import OracleUncertaintyAcquisition
from .random import RandomAcquisition


class AcquisitionFactory:
    @staticmethod
    def create(acquisition_type: str) -> Acquisition:
        match acquisition_type.lower():
            case "random":
                return RandomAcquisition()
            case "oracle_uncertainty":
                return OracleUncertaintyAcquisition(
                    config=OracleUncertaintyAcquisitionConfig(
                        confidence_propagation=False,
                    )
                )
            case _:
                raise ValueError(f"Unknown acquisition type: {acquisition_type}")
