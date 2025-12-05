import traceback
from logging import getLogger
from pathlib import Path

import torch

from cp4bal.acquisition import AcquisitionFactory
from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import (
    ActiveLearningDataset,
    DatasetSplit,
    InitialPoolSelectionType,
)
from cp4bal.dataset.factory import DatasetFactory
from cp4bal.model import ModelFactory
from cp4bal.util.auc_logger import AUCLogger
from cp4bal.util.config_builder import ConfigBuilder
from cp4bal.util.logger import init_logger
from cp4bal.util.options import Options
from cp4bal.util.seed import set_seed
from cp4bal.util.writer import CSVWriter

logger = getLogger(__name__)


def main():
    options = Options().parse()
    logger.info(f"seed: {options.args.seed}")
    rng, big_seed = set_seed(seed=options.args.seed)
    generator = torch.random.manual_seed(rng.integers(2**31))
    project_root = Path(__file__).parent.parent.parent

    # configs
    cb = ConfigBuilder().set_seed(big_seed).set_experiment_name(options.args.experiment_name)

    # config for dataset
    cb.load_dataset_config_file(project_root / options.args.dataset_config_file)

    # config for model / trainer
    cb.load_model_config_file(project_root / options.args.model_config_file)

    # config for acquisition
    cb.set_acquisition_name(options.args.acquisition_name).set_propagation(options.args.propagation)

    # config for active learning
    cb.set_budget(options.args.budget).set_round(options.args.round)

    configs = cb.build()

    # logger
    init_logger(
        log_dir=(project_root / "log" / configs.experiment.name).parent,
        log_file_name=Path(configs.experiment.name).name,
    )
    logger.info(f"{configs=}")

    # dataset
    base_ds = DatasetFactory.create(config=configs.dataset)
    ds = ActiveLearningDataset(base=base_ds, config=configs.dataset)
    ds.split().print_masks()
    ds.select_initial_pool(type_=InitialPoolSelectionType.BALANCED, rng=generator)

    # Model for Training
    model = ModelFactory.create(config=configs.model, dataset=ds)

    # Active Learning
    acquisition_method = AcquisitionFactory.create(config=configs.acquisition)
    result_writer = CSVWriter(
        file_path=project_root / "out" / configs.experiment.name / "result.csv",
    ).set_header(
        [
            "round",
            "phase",
            "num_labeled_nodes",
            "accuracy",
        ]
    )

    auc_logger = AUCLogger(log_file_path=project_root / "out" / configs.experiment.name / "auc.csv")
    for al_round in range(configs.al.num_rounds + 1):
        logger.info(f"Round {al_round + 1}/{configs.al.num_rounds + 1}")

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
        acc = AL.evaluate_model(
            model=model,
            dataset=ds,
            rg=generator,
            which=DatasetSplit.TEST,
            al_round=al_round,
            writer=result_writer,
        )
        auc_logger.record_auc(round=al_round, cumulative_budget=ds.num_train_labeled_nodes, current_accuracy=acc)

        ds = AL.acquire_samples(
            budget=configs.al.budget_per_round,
            model=model,
            acquisition=acquisition_method,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )

    logger.info(f"final AUC: {auc_logger.latest_auc:.4f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e

    logger.info("finished")
