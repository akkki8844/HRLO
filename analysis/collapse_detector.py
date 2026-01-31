import numpy as np


class CollapseDetector:
    def __init__(
        self,
        latency_z_threshold=2.5,
        entropy_drop_threshold=0.35,
        min_steps=3,
    ):
        self.latency_z_threshold = latency_z_threshold
        self.entropy_drop_threshold = entropy_drop_threshold
        self.min_steps = min_steps

    def detect(self, latency_series):
        latency_series = np.asarray(latency_series, dtype=float)

        if latency_series.size < self.min_steps:
            return {
                "collapsed": False,
                "collapse_step": None,
                "reason": "insufficient_steps",
            }

        z = self._zscore(latency_series)
        entropy_series = self._rolling_entropy(latency_series)

        spike_indices = np.where(z > self.latency_z_threshold)[0]
        entropy_drops = np.where(
            np.diff(entropy_series) < -self.entropy_drop_threshold
        )[0]

        collapse_candidates = np.intersect1d(spike_indices, entropy_drops)

        if collapse_candidates.size == 0:
            return {
                "collapsed": False,
                "collapse_step": None,
                "reason": "stable_reasoning",
            }

        collapse_step = int(collapse_candidates[0])

        return {
            "collapsed": True,
            "collapse_step": collapse_step,
            "latency_at_collapse": float(latency_series[collapse_step]),
            "z_score": float(z[collapse_step]),
            "entropy_before": float(entropy_series[collapse_step]),
            "entropy_after": float(entropy_series[collapse_step + 1])
            if collapse_step + 1 < entropy_series.size
            else None,
        }

    def _zscore(self, x):
        mean = np.mean(x)
        std = np.std(x) + 1e-9
        return (x - mean) / std

    def _rolling_entropy(self, x, window=3):
        ent = []
        for i in range(len(x)):
            start = max(0, i - window + 1)
            segment = x[start : i + 1]
            ent.append(self._entropy(segment))
        return np.array(ent)

    def _entropy(self, x):
        hist, _ = np.histogram(x, bins=min(5, len(x)), density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log2(hist))
