import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import yaml

PROJ_ROOT = Path(__file__).parent.parent
DATASET_CONFIG_PATH = "config/dataset/csbm-18.yaml"
MODEL_CONFIG_PATH = "config/model/bayes_optimal.yaml"

with open(PROJ_ROOT / DATASET_CONFIG_PATH, "r") as f:
    dataset_config = yaml.safe_load(f)
    class_num = dataset_config.get("num_classes")

total_budget = 24 * class_num

budget_round_pairs = [
    # (1, total_budget),
    # (2, total_budget // 2),
    # (4, total_budget // 4),
    # (class_num, total_budget // class_num),
    # (2*class_num, total_budget // (2*class_num)),
    # (3*class_num, total_budget // (3*class_num)),
    # (4*class_num, total_budget // (4*class_num)),
    # (6*class_num, total_budget // (6*class_num)),
    # (8*class_num, total_budget // (8*class_num)),
    # (12*class_num, total_budget // (12*class_num)),
    (24*class_num, total_budget // (24*class_num)),
]

try:
    git_root = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], 
        text=True
    ).strip()
except subprocess.CalledProcessError:
    print("not in a git repository", file=sys.stderr)
    sys.exit(1)

target_dir = os.path.join(git_root, "script")
os.chdir(target_dir)

# seeds = [28, 69, 72, 85, 116, 31, 41, 52, 94, 318]
rng = np.random.default_rng(seed=2025)
seeds = rng.choice(10000, size=90, replace=False).tolist()
methods = ["oracle_uncertainty", "oracle_uncertainty_cp"]
for budget, round_num in budget_round_pairs:
    for seed in seeds:
        for method in methods:
            cmd = [
                "sbatch",
                "job.sh",
                str(seed),
                method,
                str(budget),
                str(round_num),
                DATASET_CONFIG_PATH,
                MODEL_CONFIG_PATH
            ]
            subprocess.run(cmd)
