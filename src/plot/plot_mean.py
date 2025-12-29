import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import *  # noqa: F403
from plot.utils import (
    compute_auc_from_budgets_and_means,
    load_results,
    method_to_color,
    method_to_linestyle,
    method_to_marker,
    method_to_name,
)

TARGET_RESULTS = [
    csbm17_b8_entropy,
    csbm17_b8_us,
    csbm17_b8_usp,
    csbm17_b8_random,
    csbm17_b8_least_confidence,
    csbm17_b8_margin,
]
FIG_NAME = "csbm17-b8.png"
SHOW_STD = False

def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, result_paths in enumerate(TARGET_RESULTS):
        name, budgets, means, stds = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        ax.plot(
            budgets, means,
            label=f"{method_to_name(result_paths.method)} (AUC: {auc:.4f})",
            # label=f"{result_paths.name} (AUC: {auc:.4f})",
            marker=method_to_marker(result_paths.method),
            markersize=8,
            color=method_to_color(result_paths.method),
            linestyle=method_to_linestyle(result_paths.method),
            linewidth=3,
        )
        if SHOW_STD:
            ax.fill_between(
                budgets,
                [m - s for m, s in zip(means, stds)],
                [m + s for m, s in zip(means, stds)],
                alpha=0.2,
                color=method_to_color(result_paths.method),
            )

    ax.set_xlabel("#Annotation", fontsize=18)
    ax.set_ylabel("Accuracy", fontsize=18)
    ax.legend(fontsize=14)
    ax.tick_params(axis="both", labelsize=14)
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
