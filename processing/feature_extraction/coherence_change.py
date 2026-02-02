import numpy as np


class CoherenceChange:
    def __init__(self, window_size=5):
        self.window_size = window_size

    def compute(self, emg_signal, timestamps, step_times):
        emg_signal = np.asarray(emg_signal, dtype=float)
        timestamps = np.asarray(timestamps, dtype=float)
        step_times = np.asarray(step_times, dtype=float)

        coherence_values = []

        for step_time in step_times:
            window_mask = (
                (timestamps >= step_time - self.window_size / 2)
                & (timestamps <= step_time + self.window_size / 2)
            )

            window_signal = emg_signal[window_mask]

            if window_signal.size < 2:
                coherence_values.append(0.0)
                continue

            coherence = self._signal_coherence(window_signal)
            coherence_values.append(coherence)

        return np.array(coherence_values)

    def _signal_coherence(self, signal):
        mean = np.mean(signal)
        std = np.std(signal)

        if std == 0:
            return 0.0

        normalized = (signal - mean) / std
        coherence = 1.0 / (1.0 + np.var(normalized))

        return float(coherence)
