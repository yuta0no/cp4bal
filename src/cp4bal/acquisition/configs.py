from dataclasses import dataclass

from .enums import AcquisitionType, CoresetDistance, DegreeType, UncertaintyType


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
class CoresetAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.CORESET_FEATURE
    requires_model_predictions: bool = True
    coreset_distance: CoresetDistance = CoresetDistance.INPUT_FEATURES


@dataclass(kw_only=True)
class FeatureCoresetAcquisitionConfig(CoresetAcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.CORESET_FEATURE
    requires_model_predictions: bool = True
    coreset_distance: CoresetDistance = CoresetDistance.INPUT_FEATURES


@dataclass(kw_only=True)
class OracleUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ORACLE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC


@dataclass(kw_only=True)
class OracleUncertaintyWithConfidencePropagationAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.ORACLE_UNCERTAINTY_CP
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC


@dataclass(kw_only=True)
class ApproximateUncertaintyAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.APPROXIMATE_UNCERTAINTY
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC
    # whether to compute aleatoric confidence of a node when leaving it out (which is more exact, but way more costly)
    aleatoric_confidence_with_left_out_node: bool = False
    # How often to draw samples from the predictive distribution as truth for aleatoric confidence
    # If None, use the argmax label
    aleatoric_confidence_labels_num_samples: int | None = None
    # if True, conf(epi) is computed as conf(total) / conf(ale)
    # if False, we optimize the ratio of observing the remaining expected ground-truth
    compute_as_ratio: bool = True


@dataclass(kw_only=True)
class ApproximateUncertaintyWithConfidencePropagationAcquisitionConfig(AcquisitionConfig):
    type_: AcquisitionType = AcquisitionType.APPROXIMATE_UNCERTAINTY_CP
    uncertainty_type: UncertaintyType = UncertaintyType.EPISTEMIC
    aleatoric_confidence_with_left_out_node: bool = False
    aleatoric_confidence_labels_num_samples: int | None = None
    compute_as_ratio: bool = True

@dataclass(kw_only=True)
class AcquisitionByAttributeConfig(AcquisitionConfig):
    higher_is_better: bool
    type_: AcquisitionType = AcquisitionType.BY_ATTRIBUTE

@dataclass(kw_only=True)
class DegreeAcquisitionConfig(AcquisitionByAttributeConfig):
    type_: AcquisitionType = AcquisitionType.DEGREE
    requires_model_predictions: bool = False
    higher_is_better: bool = True
    degree_type: DegreeType = DegreeType.IN

@dataclass(kw_only=True)
class EnergyAcquisitionConfig(AcquisitionByAttributeConfig):
    type_: AcquisitionType = AcquisitionType.ENERGY
    requires_model_predictions: bool = True
    higher_is_better: bool = True
    temperature: float = 1.0

@dataclass(kw_only=True)
class EntropyAcquisitionConfig(AcquisitionByAttributeConfig):
    type_: AcquisitionType = AcquisitionType.ENTROPY
    requires_model_predictions: bool = True
    higher_is_better: bool = True

@dataclass(kw_only=True)
class MarginAcquisitionConfig(AcquisitionByAttributeConfig):
    type_: AcquisitionType = AcquisitionType.MARGIN
    requires_model_predictions: bool = True
    higher_is_better: bool = True

@dataclass(kw_only=True)
class LeastConfidenceAcquisitionConfig(AcquisitionByAttributeConfig):
    type_: AcquisitionType = AcquisitionType.LEAST_CONFIDENCE
    requires_model_predictions: bool = True
    higher_is_better: bool = True
