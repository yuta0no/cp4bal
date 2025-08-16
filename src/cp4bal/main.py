from logging import getLogger
from pathlib import Path

import torch

from cp4bal.acquisition import AcquisitionFactory
from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import CSBM, ActiveLearningDataset
from cp4bal.model import GCN
from cp4bal.util.configs import ActiveLearningConfig, CSBMConfig, DatasetConfig, GCNConfig, TrainerConfig
from cp4bal.util.enums import DatasetSplit, EdgeProbabilityType, TrainerType
from cp4bal.util.logger import init_logger
from cp4bal.util.seed import set_seed

logger = getLogger(__name__)


def main():
    rng, big_seed = set_seed(seed=52)
    generator = torch.random.manual_seed(rng.integers(2**31))

    # Dataset
    ds_config = DatasetConfig(
        seed=big_seed, name="csbm", num_nodes=240, num_classes=6, dim_features=10, val_size=0.1, test_size=0.1
    )
    csbm = CSBM(
        common_config=ds_config,
        csbm_config=CSBMConfig(
            feature_sigma=1.0,
            feature_class_mean_distance=1.0,
            edge_p_type=EdgeProbabilityType.BY_SNR_AND_DEGREE,
            p_edge_inter=None,
            p_edge_intra=None,
            expected_degree=8,
            edge_p_snr=10,
        ),
    )
    ds = ActiveLearningDataset(base=csbm, config=ds_config)
    ds.split().print_masks()
    ds.select_initial_pool(count_per_class=1)

    # Model
    model = GCN(config=GCNConfig())
    logger.info(f"model: {model}")

    # Active Learning
    acquisition_method = AcquisitionFactory.create(acquisition_type="random")

    ds.select_initial_pool(count_per_class=1)
    TOTAL_AL_ROUND = 5
    for al_round in range(TOTAL_AL_ROUND):
        logger.info(f"Round {al_round + 1}/{TOTAL_AL_ROUND}")

        dataset = AL.acquire_samples(
            config=ActiveLearningConfig(
                acquisition_type="random",
                num_rounds=TOTAL_AL_ROUND,
                budget_per_round=ds_config.common.num_classes,
                num_epochs=100,
                trainer_type="sgd",
            ),
            model=model,
            acquisition=acquisition_method,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )

        AL.train_model(
            config=TrainerConfig(
                name=TrainerType.SGD,
                reset_parameter_before_training=True,
                progress_bar=True,
                use_gpu=True,
                verbose=True,
            ),
            model=model,
            dataset=dataset,
            rg=generator,
            al_round=al_round,
        )

        AL.evaluate_model(
            model=model,
            dataset=dataset,
            rg=generator,
            which=DatasetSplit.VAL,
            al_round=al_round,
        )
        AL.evaluate_model(
            model=model,
            dataset=dataset,
            rg=generator,
            which=DatasetSplit.TEST,
            al_round=al_round,
        )


if __name__ == "__main__":
    init_logger(log_dir=Path("logs"), log_file_name="cp4bal")
    try:
        main()
    except Exception as e:
        logger.error(f"error occurred: {e}")

    logger.info("finished")
