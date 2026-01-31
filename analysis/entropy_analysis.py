import numpy as np

class EntropyAnalysis:
    def __init__(self, window_size=3):
        self.window_size = window_size

    def compute_step_entropy(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)
        entropy_values = []

        for i in range(len(latency_series)):
            start = max(0, i - self.window_size + 1)
            window = latency_series[start : i + 1]
            entropy_values.append(self._entropy(window))

        return np.array(entropy_values)
    
    def compute_global_entropy(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)
        return self._entropy(latency_series)
    
    def _entropy(self, values):
        if len(values) == 0:
            return 0.0

        hist, _ = np.histogram(
            values, bins=min(len(values), 5), density=True
        )
        hist = hist[hist > 0]

        if hist.size == 0:
            return 0.0
        
        return -np.sum(hist * np.log2(hist))