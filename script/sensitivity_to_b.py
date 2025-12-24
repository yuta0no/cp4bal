import os
import subprocess
import sys

DATASET_CONFIG = "config/dataset/csbm-13.yaml"
MODEL_CONFIG = "config/model/bayes_optimal.yaml"

budget_round_pairs = [
    (24, 2),
    (16, 3),
    (12, 4),
    (8, 6),
    (6, 8),
    (4, 12),
    (3, 16),
    (2, 24),
    (1, 48),
    # (32, 3),
    # (24, 4),
    # (16, 6),
    # (8, 12),
    # (4, 24),
    # (2, 48),
    # (1, 96),
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

seeds = [28, 69, 72, 85, 116, 31, 41, 52, 94, 318]
methods = ["oracle_uncertainty", "oracle_uncertainty_cp", "random"]
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
                DATASET_CONFIG,
                MODEL_CONFIG
            ]
            subprocess.run(cmd)