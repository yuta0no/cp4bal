import matplotlib.pyplot as plt
import numpy as np

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import compute_auc_from_budgets_and_means, get_n_continuous_colors, load_results

# Parameters
CLASS_NUM = 4
TARGET_RESULTS = [
    b_sensitivity_csbm8_b1,
    b_sensitivity_csbm8_b2,
    b_sensitivity_csbm8_b3,
    b_sensitivity_csbm8_b4,
    b_sensitivity_csbm8_b6,
    b_sensitivity_csbm8_b8,
    b_sensitivity_csbm8_b12,
    b_sensitivity_csbm8_b16,
    b_sensitivity_csbm8_b24,
]
FIG_NAME = "b_sensitivity_csbm8.png"
# Consants for plot
Y_MAX = 0.725
Y_MIN = 0.50

def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    cs = get_n_continuous_colors(len(TARGET_RESULTS), cmap_name="coolwarm")
    for result_paths, color in zip(TARGET_RESULTS, cs):
        name, budgets, means, _ = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        if len(name) == 1:
            name += "  "
        name = f"{name} (AUC: {auc:.3f})"
        ax.plot(budgets, means, marker="o", label=name, color=color)

    ax.set_xlabel("#Annotation", fontsize=18)
    ax.set_ylabel("Accuracy", fontsize=18)
    xticks = np.arange(min(budgets), max(budgets) + CLASS_NUM, CLASS_NUM)
    ax.set_xticks(xticks)
    # ax.set_ylim(Y_MIN, Y_MAX)
    ax.legend(fontsize=14)
    ax.tick_params(axis="both", labelsize=14)
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
