from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from plot.constant import FIG_DIR


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


TARGET_RESULTS = []

def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, _ = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    fig.savefig(FIG_DIR / "mean_accuracy_new.png")


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
