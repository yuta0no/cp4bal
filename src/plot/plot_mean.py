from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


random = ResultPaths(
    name="random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:22:39-08a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:22:43-a8f4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:22:48-24c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:22:53-707c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:22:58-87f9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:23:02-13bd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:23:07-fd7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:23:12-a803/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:23:16-f21b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T14:23:21-c40b/result.csv",
    ],
)

us = ResultPaths(
    name="uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:13:44-7de5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:14:08-e0ce/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:14:31-aa58/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:14:55-253d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:15:19-021b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:15:42-d188/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:16:06-c23c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:16:29-dba3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:16:53-10de/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T14:17:20-05cb/result.csv",
    ]
)

TARGET_RESULTS = [random, us]

def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, stds = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    fig.savefig(FIG_DIR / "mean_accuracy.png")


def load_results(result_paths: ResultPaths) -> tuple[str, list[int], list[float], list[float]]:
    all_data = [pd.read_csv(path) for path in result_paths.paths]
    combined = pd.concat(all_data, ignore_index=True).groupby(["round", "phase"])
    stats = combined[["accuracy", "num_labeled_nodes"]].agg(["mean", "std"]).reset_index()
    budgets = stats["num_labeled_nodes"]["mean"].tolist()
    means = stats["accuracy"]["mean"].tolist()
    stds = stats["accuracy"]["std"].tolist()
    return result_paths.name, budgets, means, stds


if __name__ == "__main__":
    main()
