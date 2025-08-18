from logging import ERROR, WARNING, getLogger
from logging.config import dictConfig
from pathlib import Path

import yaml

DEFAULT_LOGGER_CONFIG = Path(__file__).parent / "logger_config.yaml"


def init_logger(log_dir: Path, log_file_name: str, config_path: Path = DEFAULT_LOGGER_CONFIG) -> None:
    with config_path.open(mode="r") as f:
        config = yaml.safe_load(f)
        log_path = log_dir / f"{log_file_name}.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        config["handlers"]["file"]["filename"] = str(log_path)
        dictConfig(config)
    getLogger("matplotlib").setLevel(WARNING)  # surpress unnecessary logging
    getLogger("sklearn").setLevel(ERROR)  # surpress unnecessary logging
    getLogger("numba").setLevel(WARNING)  # surpress unnecessary logging
