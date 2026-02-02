import numpy as np


class NormalizeLatency:
    def __init__(self, method="zscore"):
        self.method = method

    def normalize(self, latency_series, baseline_profile=None):
        latency_series = np.asarray(latency_series, dtype=float)

        if latency_series.size == 0:
            return latency_series

        if self.method == "zscore":
            mean = np.mean(latency_series)
            std = np.std(latency_series) + 1e-9
            return (latency_series - mean) / std

        if self.method == "baseline" and baseline_profile is not None:
            mean = baseline_profile.get("mean_latency", np.mean(latency_series))
            std = baseline_profile.get("std_latency", np.std(latency_series)) + 1e-9
            return (latency_series - mean) / std

        if self.method == "minmax":
            min_v = np.min(latency_series)
            max_v = np.max(latency_series)
            if max_v == min_v:
                return np.zeros_like(latency_series)
            return (latency_series - min_v) / (max_v - min_v)

        return latency_series
