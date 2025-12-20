from .approximate_uncertainty import ApproximateUncertaintyAcquisition
from .configs import ApproximateUncertaintyAcquisitionConfig


class ApproximateUncertaintyWithConfidencePropagationAcquisition(ApproximateUncertaintyAcquisition):
    def __init__(self, config: ApproximateUncertaintyAcquisitionConfig):
        super().__init__(config=config)
        self.confidence_propagation = True
