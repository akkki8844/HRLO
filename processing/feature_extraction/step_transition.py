import numpy as np


class StepTransition:
    def __init__(self):
        pass

    def compute(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)

        if latency_series.size < 2:
            return {
                "transitions": [],
                "transition_strength": [],
            }

        transitions = np.diff(latency_series)
        strengths = self._transition_strength(transitions)

        return {
            "transitions": transitions.tolist(),
            "transition_strength": strengths.tolist(),
        }

    def _transition_strength(self, transitions):
        mean = np.mean(transitions)
        std = np.std(transitions)

        if std == 0:
            return np.zeros_like(transitions)

        return np.abs((transitions - mean) / std)
