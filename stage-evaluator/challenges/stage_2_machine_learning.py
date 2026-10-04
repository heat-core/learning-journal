"""
Stage 2 Challenge: Applied Statistics & Classical Machine Learning
Gate 2 Focus: Feature Scaling without Data Leakage & Pure Metrics (Project P1)
"""
from typing import List, Tuple, Dict
import math

class SafeStandardScaler:
    """
    StandardScaler implemented strictly separating fit and transform to avoid data leakage.
    """
    def __init__(self):
        self.mean_ = None
        self.std_ = None

    def fit(self, data: List[float]):
        if not data:
            raise ValueError("Data cannot be empty")
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std = math.sqrt(variance)
        if std == 0.0:
            std = 1.0  # Prevent divide by zero
        self.mean_ = mean
        self.std_ = std
        return self

    def transform(self, data: List[float]) -> List[float]:
        if self.mean_ is None or self.std_ is None:
            raise RuntimeError("Scaler has not been fitted yet")
        return [(x - self.mean_) / self.std_ for x in data]

    def fit_transform(self, data: List[float]) -> List[float]:
        return self.fit(data).transform(data)


class ClassificationMetrics:
    """
    Pure Python calculation of confusion matrix and metrics (Precision, Recall, F1).
    """
    @staticmethod
    def compute(y_true: List[int], y_pred: List[int]) -> Dict[str, float]:
        if len(y_true) != len(y_pred) or not y_true:
            raise ValueError("Arrays must be non-empty and of equal length")

        tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
        fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
        fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
        tn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        accuracy = (tp + tn) / len(y_true)

        return {
            "tp": tp, "fp": fp, "fn": fn, "tn": tn,
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
        }
