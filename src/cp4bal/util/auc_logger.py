from pathlib import Path

import numpy as np


class AUCLogger:
    def __init__(self, log_file_path: Path):
        self.log_file_path = log_file_path
        self.log_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.budgets = [0]
        self.accuracies = [0.0]
        with open(self.log_file_path, "w") as f:
            f.write("round,budget,auc\n")

    def record_auc(self, round: int, cumulative_budget: float, current_accuracy: float):
        """Records the AUC for the current round.
        
        Parameters
        ----------
        round : int
            The current round number.
        cumulative_budget : float
            The cumulative budget used up to this round.
        current_accuracy : float
            The accuracy achieved at this round (0 <= acc <= 1).
        """
        auc = self._calculate_auc(cumulative_budget, current_accuracy)
        with open(self.log_file_path, "a") as f:
            f.write(f"{round},{cumulative_budget},{auc}\n")

    def _calculate_auc(self, cumulative_budget: int, current_accuracy: float) -> float:
        self.budgets.append(cumulative_budget)
        self.accuracies.append(current_accuracy)
        auc = np.trapezoid(self.accuracies, self.budgets) / max(self.budgets)
        return auc
