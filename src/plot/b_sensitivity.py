import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import (
    b_sensitivity_csbm4_b1,
    b_sensitivity_csbm4_b2,
    b_sensitivity_csbm4_b3,
    b_sensitivity_csbm4_b4,
    b_sensitivity_csbm4_b6,
    b_sensitivity_csbm4_b8,
    b_sensitivity_csbm4_b12,
    b_sensitivity_csbm4_b24,
)
from plot.utils import get_n_continuous_colors, load_results

TARGET_RESULTS = [
    b_sensitivity_csbm4_b1,
    b_sensitivity_csbm4_b2,
    b_sensitivity_csbm4_b3,
    b_sensitivity_csbm4_b4,
    b_sensitivity_csbm4_b6,
    b_sensitivity_csbm4_b8,
    b_sensitivity_csbm4_b12,
    b_sensitivity_csbm4_b24,
]
FIG_NAME = "b_sensitivity_csbm4.png"


def main():
    fig, ax = plt.subplots()
    cs = get_n_continuous_colors(len(TARGET_RESULTS), cmap_name="inferno")
    for result_paths, color in zip(TARGET_RESULTS, cs):
        name, budgets, means, _ = load_results(result_paths)
        ax.plot(budgets, means, marker="o", label=name, color=color)

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
