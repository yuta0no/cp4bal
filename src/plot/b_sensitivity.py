import math

import matplotlib.pyplot as plt
import numpy as np

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import compute_auc_from_budgets_and_means, get_n_continuous_colors, load_results

# Parameters
CLASS_NUM = 4
TARGET_RESULTS = [
    b_sensitivity_csbm10_b4_wocp,
    b_sensitivity_csbm10_b8_wocp,
    b_sensitivity_csbm10_b12_wocp,
    b_sensitivity_csbm10_b24_wocp,
]
FIG_NAME = "b_sensitivity_csbm10_wocp.png"
# Consants for plot
Y_MAX = 0.725
Y_MIN = 0.50
SHOW_LB = False  # 1-1/e lower bound


def main():
    fig, ax = plt.subplots(figsize=(10, 6))
    cs = get_n_continuous_colors(len(TARGET_RESULTS), cmap_name="coolwarm")
    handle_dict = {}
    for result_paths, color in zip(TARGET_RESULTS, cs):
        name, budgets, means, _ = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        if len(name) == 1:
            name += "  "
        name = f"{name} (AUC: {auc:.3f})"
        line = ax.plot(budgets, means, marker="o", label=name, color=color)
        handle_dict[budgets[1] - budgets[0]] = line[0]
        if (budgets[0] == budgets[1] - 1) and SHOW_LB:
            lower_bound = _calculate_lb(means)
            line = ax.plot(budgets, lower_bound, linestyle="--", color="black", linewidth=2, label="Theoretical Lower Bound")
            handle_dict[100] = line[0]
    ax.set_xlabel("#Annotation", fontsize=18)
    ax.set_ylabel("Accuracy", fontsize=18)
    xticks = np.arange(min(budgets), max(budgets) + CLASS_NUM, CLASS_NUM)
    ax.set_xticks(xticks)
    # ax.set_ylim(Y_MIN, Y_MAX)

    # legend
    handles = [handle_dict[key] for key in sorted(handle_dict.keys())]
    ax.legend(handles=handles, bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0, fontsize=14)

    ax.tick_params(axis="both", labelsize=14)
    fig.tight_layout()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


def _calculate_lb(means):
    a0 = means[0]
    lower_bounds = [a0]
    for i in range(1, len(means)):
        ai = means[i]
        lb = ai * (ai / a0) ** (-1 / math.e)
        lower_bounds.append(lb)
    return lower_bounds


if __name__ == "__main__":
    main()
