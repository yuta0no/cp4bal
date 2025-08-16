from dataclasses import dataclass

from .enums import AcquisitionType, UncertaintyType


@dataclass
class AcquisitionConfig:
    type_: AcquisitionType
    requires_model_predictions: bool = False


@dataclass
class RandomAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.RANDOM
    requires_model_predictions: bool = False


@dataclass
class EntropyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ENTROPY
    requires_model_predictions: bool = True


@dataclass
class OracleUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ORACLE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC
