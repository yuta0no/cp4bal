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


@dataclass(kw_only=True)
class ApproximateUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.APPROXIMATE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC
    confidence_propagation: bool = False
    # whether to compute aleatoric confidence of a node when leaving it out (which is more exact, but way more costly)
    aleatoric_confidence_with_left_out_node: bool = False
    # How often to draw samples from the predictive distribution as truth for aleatoric confidence
    # If None, use the argmax label
    aleatoric_confidence_labels_num_samples: int | None = None
    # if True, conf(epi) is computed as conf(total) / conf(ale)
    # if False, we optimize the ratio of observing the remaining expected ground-truth
    compute_as_ratio: bool = True
