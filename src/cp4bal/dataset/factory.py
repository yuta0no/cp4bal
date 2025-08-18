from .configs import DatasetConfig
from .csbm import CSBM


class DatasetFactory:
    @staticmethod
    def create(config: DatasetConfig) -> CSBM:
        if config.common.name == "csbm":
            return CSBM(
                common_config=config.common,
                csbm_config=config.detail,
            )
        else:
            raise ValueError(f"Unknown dataset name: {config.common.name}")
