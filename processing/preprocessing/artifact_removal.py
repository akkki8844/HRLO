import numpy as np


class ArtifactRemoval:
    def __init__(self, z_threshold=3.0):
        self.z_threshold = z_threshold

    def clean(self, signal):
        signal = np.asarray(signal, dtype=float)

        if signal.size == 0:
            return signal

        mean = np.mean(signal)
        std = np.std(signal)

        if std == 0:
            return signal

        z_scores = (signal - mean) / std
        cleaned = signal.copy()

        outliers = np.abs(z_scores) > self.z_threshold

        if np.any(outliers):
            cleaned[outliers] = self._interpolate(signal, outliers)

        return cleaned

    def _interpolate(self, signal, mask):
        indices = np.arange(signal.size)
        valid = ~mask

        if valid.sum() < 2:
            return signal[mask]

        return np.interp(indices[mask], indices[valid], signal[valid])
