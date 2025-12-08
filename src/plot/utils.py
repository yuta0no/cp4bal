import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot.results import ResultPaths
from plot.types_ import ActiveLearningMethod as ALM


def load_results(result_paths: ResultPaths) -> tuple[str, list[int], list[float], list[float]]:
    all_data = [pd.read_csv(path) for path in result_paths.paths]
    combined = pd.concat(all_data, ignore_index=True).groupby(["round", "phase"])
    stats = combined[["accuracy", "num_labeled_nodes"]].agg(["mean", "std"]).reset_index()
    budgets = stats["num_labeled_nodes"]["mean"].tolist()
    means = stats["accuracy"]["mean"].tolist()
    stds = stats["accuracy"]["std"].tolist()
    return result_paths.name, budgets, means, stds


def get_n_continuous_colors(n: int, cmap_name: str = 'viridis') -> list:
    intervals = np.linspace(0, 1, n)
    cmap = plt.get_cmap(cmap_name)
    return cmap(intervals).tolist()


def compute_auc_from_budgets_and_means(budgets: list[int], means: list[float]) -> float:
    auc = 0.0
    auc_max = (budgets[-1] - budgets[0]) * 1.0
    for i in range(1, len(budgets)):
        x_diff = budgets[i] - budgets[i - 1]
        y_avg = (means[i] + means[i - 1]) / 2
        auc += x_diff * y_avg
    return auc / auc_max


def method_to_color(method: ALM) -> str:
    color_map = {
        ALM.RANDOM: "gray",
        ALM.ORACLE_UNCERTAINTY_CP: "green",
        ALM.ORACLE_UNCERTAINTY: "purple",
    }
    return color_map.get(method, "black")


def method_to_linestyle(method: ALM) -> str:
    linestyle_map = {
        ALM.RANDOM: "dashed",
    }
    return linestyle_map.get(method, "solid")


def method_to_marker(method: ALM) -> str:
    marker_map = {
        ALM.RANDOM: "o",
        ALM.ORACLE_UNCERTAINTY_CP: "s",
        ALM.ORACLE_UNCERTAINTY: "D",
    }
    return marker_map.get(method, "x")


def method_to_name(method: ALM) -> str:
    name_map = {
        ALM.RANDOM: "Random",
        ALM.ORACLE_UNCERTAINTY_CP: "Ours",
        ALM.ORACLE_UNCERTAINTY: "Uncertainty",
    }
    return name_map.get(method, "Unknown Method")