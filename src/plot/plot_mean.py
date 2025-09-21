from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


uncertainty_w_initial7 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-19T11:50:07-53a6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-19T11:50:10-5eb7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-19T11:50:11-ff70/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-19T19:04:09-8fae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-19T19:13:17-242c/result.csv",
    ]
)

uncertainty_w_initial1 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-20T14:49:59-35cf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-20T14:50:01-0e44/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-20T14:50:01-36d9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-20T14:50:01-d0ce/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/oracle_uncertainty/2025-09-20T14:50:01-ed03/result.csv",
    ]
)
random_w_initial7 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-19T11:50:07-f660/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-19T11:50:13-811e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-19T11:50:14-54b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-19T19:13:16-5fea/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-19T20:38:32-8c00/result.csv",
    ]
)

random_w_initial1 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-20T14:49:59-1f2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-20T14:50:01-2b63/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-20T14:50:01-bdc8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-20T14:50:01-fa48/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/1/random/2025-09-20T14:51:07-6f54/result.csv",
    ]
)

TARGET_RESULTS = [random_w_initial7, uncertainty_w_initial7]


def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, stds = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")
        ax.fill_between(
            budgets,
            [m - s for m, s in zip(means, stds)],
            [m + s for m, s in zip(means, stds)],
            alpha=0.2,
        )

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    fig.savefig(FIG_DIR / "mean_accuracy_w_initial7.png")


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
