from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


# batch size = 1, initial pool size = 7 (random)
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
# batch size = 1, initial pool size = 1 (random)
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
# batch size = 7, initial pool size = 7 (random)
uncertainty_batch_7_initial_random_7 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T22:36:35-12e3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T22:36:36-2f4c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T22:36:38-50c3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T22:36:38-fd43/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T22:37:39-8173/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-22T09:34:35-6a07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-22T09:34:36-2d70/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-22T09:34:38-946a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-22T09:34:38-a8a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-22T09:34:38-ed67/result.csv",
    ]
)

# batch size = 7, initial pool size = 7 (1 per class)
uncertainty_batch_7_initial_balanced_7 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T15:45:06-225b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T15:45:10-5d63/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T15:45:10-a606/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T15:45:10-e9fd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-09-21T15:45:10-fe7b/result.csv",
    ]
)

cp4bal_7_w_initial_balanced_7 = ResultPaths(
    name="ours",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T19:51:52-40d7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T19:51:52-45f0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T19:51:52-aeed/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T19:51:52-cec9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T19:51:52-e3b4/result.csv",
    ]
)

cp4bal_7_w_initial_random_7 = ResultPaths(
    name="ours",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T22:37:39-3cd5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T22:37:39-3e1d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T22:37:39-6a4b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T22:37:39-b8fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-21T22:40:06-bbaa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-22T09:33:43-1dd8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-22T09:33:43-7ee3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-22T09:33:43-81d4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-22T09:33:43-a517/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-09-22T09:33:43-e3e5/result.csv",
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

random_batch_7_initial_random_7 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T22:36:35-e7d1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T22:36:36-e46b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T22:36:37-b57d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T22:36:38-645c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T22:37:39-c3c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-22T09:34:35-c850/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-22T09:34:36-5cc7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-22T09:34:36-b216/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-22T09:34:38-40e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-22T09:34:38-a613/result.csv",
    ]
)

random_batch_7_initial_balanced_7 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T15:45:04-8fd0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T15:45:10-0b65/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T15:45:10-2ecb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T15:45:10-d271/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-09-21T15:45:10-dd71/result.csv",
    ]
)

TARGET_RESULTS = [cp4bal_7_w_initial_random_7, uncertainty_batch_7_initial_random_7, random_batch_7_initial_random_7]
FIG_NAME = "mean_accuracy_batch_7_initial_random_7.png"

def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, stds = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")
        # ax.fill_between(
        #     budgets,
        #     [m - s for m, s in zip(means, stds)],
        #     [m + s for m, s in zip(means, stds)],
        #     alpha=0.2,
        # )

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    fig.savefig(FIG_DIR / FIG_NAME)


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
