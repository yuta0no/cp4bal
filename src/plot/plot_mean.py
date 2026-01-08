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
    csbm19_b32_degree,
    csbm19_b32_energy,
    csbm19_b32_entropy,
    csbm19_b32_us,
    csbm19_b32_usp,
    csbm19_b32_random,
    csbm19_b32_least_confidence,
    csbm19_b32_margin,
]
EXTS = ["png", "pdf"]
FIG_NAME = "csbm19-b32-comp"
SHOW_STD = True

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
    ax.legend(fontsize=14, loc="upper left")
    ax.tick_params(axis="both", labelsize=14)
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    for ext in EXTS:
        fig.savefig(FIG_DIR / "accuracy" / f"{FIG_NAME}_accuracy.{ext}", dpi=300)


if __name__ == "__main__":
    main()
