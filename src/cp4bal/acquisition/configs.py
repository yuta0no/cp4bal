from dataclasses import dataclass

from .enums import AcquisitionType, UncertaintyType


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
class OracleUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ORACLE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC
    confidence_propagation: bool = True
