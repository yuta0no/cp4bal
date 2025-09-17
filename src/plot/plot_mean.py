from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


random_s_snr2 = ResultPaths(
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

random_s_snr10 = ResultPaths(
    name="random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:12:54-6806/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:00-1d30/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:04-d902/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:09-6ac6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:14-7821/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:19-2149/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:24-a71a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:30-e69d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:35-5cb7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/random/2025-09-17T15:13:40-c25e/result.csv",
    ]
)

us_s_snr2 = ResultPaths(
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

us_s_snr10 = ResultPaths(
    name="uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:15:13-0609/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:15:48-5f0b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:16:23-1412/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:16:58-2a8f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:17:35-28a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:18:10-5f41/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:18:47-5c80/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:19:23-6811/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:20:00-eb9f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/sgc/1/approximate_uncertainty/2025-09-17T15:20:36-bf5e/result.csv",
    ]
)

TARGET_RESULTS = [random_s_snr10, us_s_snr10]

def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, _ = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    fig.savefig(FIG_DIR / "mean_accuracy_s_snr10.png")


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
