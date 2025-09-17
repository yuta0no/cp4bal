import traceback
from logging import getLogger
from math import ceil, log
from pathlib import Path

import torch

from cp4bal.acquisition import AcquisitionFactory
from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import (
    ActiveLearningDataset,
    DatasetSplit,
    InitialPoolSelectionType,
)
from cp4bal.dataset.enums import EdgeProbabilityType
from cp4bal.dataset.factory import DatasetFactory
from cp4bal.model import ModelFactory
from cp4bal.util.config_builder import ConfigBuilder
from cp4bal.util.logger import init_logger
from cp4bal.util.options import Options
from cp4bal.util.seed import set_seed
from cp4bal.util.writer import CSVWriter

logger = getLogger(__name__)


def main():
    options = Options().parse()
    logger.info(f"seed: {options.args.seed}")
    rng, big_seed = set_seed(seed=options.args.seed)  # 42, 552
    generator = torch.random.manual_seed(rng.integers(2**31))

    # configs
    cb = ConfigBuilder().set_seed(big_seed).set_experiment_name(options.args.experiment_name)

    # config for dataset
    n_class = 7
    n_nodes = 100
    dim_feature = max(n_class, ceil(n_nodes / (log(n_nodes) * log(n_nodes))))
    cb.set_ds_name("csbm").set_n_nodes(n_nodes).set_n_classes(n_class).set_dim_features(dim_feature).set_val_size(
        0.0
    ).set_test_size(0.2).set_feature_sigma(1.0).set_feature_class_mean_distance(0.2).set_edge_p_type(
        EdgeProbabilityType.BY_SNR_AND_DEGREE
    ).set_expected_degree(8).set_edge_p_snr(3.0)

    # config for trainer
    cb.set_trainer_name("oracle")

    # config for model
    cb.set_model_name("bayes_optimal")

    # config for acquisition
    cb.set_acquisition_name(options.args.acquisition_name).set_propagation(options.args.propagation)

    # config for active learning
    cb.set_budget(options.args.budget).set_round(options.args.round)

    configs = cb.build(config_path=Path(""))
    init_logger(
        log_dir=(Path(__file__).parent.parent.parent / "log" / configs.experiment.name).parent,
        log_file_name=Path(configs.experiment.name).name,
    )
    logger.info(f"{configs=}")

    # Dataset
    base_ds = DatasetFactory.create(config=configs.dataset)
    ds = ActiveLearningDataset(base=base_ds, config=configs.dataset)
    ds.split().print_masks()
    ds.select_initial_pool(type_=InitialPoolSelectionType.BALANCED)

    # Model for Training
    model = ModelFactory.create(config=configs.model, dataset=ds)

    # Active Learning
    acquisition_method = AcquisitionFactory.create(config=configs.acquisition)
    result_writer = CSVWriter(
        file_path=Path(__file__).parent.parent.parent
        / "out"
        / configs.experiment.name
        / "result.csv",
    ).set_header(
        [
            "round",
            "phase",
            "num_labeled_nodes",
            "accuracy",
        ]
    )

    for al_round in range(configs.al.num_rounds):
        logger.info(f"Round {al_round + 1}/{configs.al.num_rounds}")

        AL.train_model(
            trainer_config=configs.trainer,
            model=model,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )

        AL.evaluate_model(
            model=model,
            dataset=ds,
            rg=generator,
            which=DatasetSplit.VAL,
            al_round=al_round,
            writer=result_writer,
        )
        AL.evaluate_model(
            model=model,
            dataset=ds,
            rg=generator,
            which=DatasetSplit.TEST,
            al_round=al_round,
            writer=result_writer,
        )

        ds = AL.acquire_samples(
            budget=configs.al.budget_per_round,  # TODO
            model=model,
            acquisition=acquisition_method,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e

    logger.info("finished")
