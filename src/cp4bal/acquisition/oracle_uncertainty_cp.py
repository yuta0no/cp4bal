from .configs import OracleUncertaintyAcquisitionConfig
from .oracle_uncertainty import OracleUncertaintyAcquisition


class OracleUncertaintyWithConfidencePropagationAcquisition(OracleUncertaintyAcquisition):
    def __init__(self, config: OracleUncertaintyAcquisitionConfig):
        super().__init__(config)
        self.confidence_propagation = True
