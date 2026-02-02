import numpy as np


class LatencyEntropy:
    def __init__(self, window_size=3, max_bins=5):
        self.window_size = window_size
        self.max_bins = max_bins

    def compute(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)

        if latency_series.size == 0:
            return np.array([])

        entropy_values = []

        for i in range(latency_series.size):
            start = max(0, i - self.window_size + 1)
            window = latency_series[start : i + 1]
            entropy_values.append(self._entropy(window))

        return np.array(entropy_values)

    def global_entropy(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)
        return self._entropy(latency_series)

    def _entropy(self, values):
        if values.size == 0:
            return 0.0

        bins = min(self.max_bins, values.size)
        hist, _ = np.histogram(values, bins=bins, density=True)
        hist = hist[hist > 0]

        if hist.size == 0:
            return 0.0

        return float(-np.sum(hist * np.log2(hist)))
