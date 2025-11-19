from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


csbm1_random_budget7_round5 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-32e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-48ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-f4f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:54-280f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:54-c29f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:54-0b07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:54-bd97/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:56-2e53/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:58-f37c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:58-fbf8/result.csv",
    ],
)

csbm1_us_budget7_round5 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:34:40-b41c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:34:48-cb4a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:35:06-8e6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:35:15-bf5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:38:35-6f83/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-3c3b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-8c2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-62a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-8248/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:03:27-69f2/result.csv",
    ]
)

csbm1_uscp_budget7_round5 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-16b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-4539/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-f221/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:54-51ce/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:54-8974/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:54-ab8a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:56-54b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:57-3b99/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:58-0c2e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:58-a81e/result.csv",
    ]
)

# CSBM-1, Budget=4, Round=9
csbm1_random_budget4_round9 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:12-9549/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-9073/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-c294/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-da24/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:15-dcc1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:15-f359/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-05c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-70e3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-097f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-fac3/result.csv",
    ],
)

csbm1_us_budget4_round9 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:29:07-c0c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:29:07-c83e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-4b8e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-39ec/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-981e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-2597/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-e188/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-f976/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:46:37-8b7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:46:49-2790/result.csv",
    ]
)

csbm1_uscp_budget4_round9 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:12-efbc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:14-14d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:14-afa7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:15-51b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:15-4440/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:16-4e87/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-76b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-93a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-2618/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-b575/result.csv",
    ]
)

# CSBM-2, Budget=7, Round=5
csbm2_random_budget7_round5 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-9c7a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-8929/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-afd3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:47-e2ee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:55:39-b99d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:56:51-1532/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:58:04-ffd7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:58:15-e95e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T18:00:59-bcfa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T18:01:23-1845/result.csv",
    ],
)

csbm2_us_budget7_round5 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:01:43-c270/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-5e3c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-8b2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-b6b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:22-79d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:34-abe4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:35-060e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:36-58a0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:49-f4cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:50-3fbd/result.csv",
    ]
)

csbm2_uscp_budget7_round5 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-3d05/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-b80b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-cc45/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-f99b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:54:54-0f39/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:56:40-c2ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:57:07-301f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:58:11-b2e0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:58:35-7261/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T18:01:17-e010/result.csv",
    ]
)

TARGET_RESULTS = [csbm2_random_budget7_round5, csbm2_us_budget7_round5, csbm2_uscp_budget7_round5]
FIG_NAME = "csbm2_budget7_round5.png"

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
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


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
