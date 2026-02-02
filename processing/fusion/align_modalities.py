import numpy as np


class ModalityAligner:
    def __init__(self):
        pass

    def align_emg_to_steps(self, emg_signal, emg_timestamps, step_timestamps, window_sec=0.2):
        emg_signal = np.asarray(emg_signal, dtype=float)
        emg_timestamps = np.asarray(emg_timestamps, dtype=float)
        step_timestamps = np.asarray(step_timestamps, dtype=float)

        aligned = []

        for step_time in step_timestamps:
            mask = (
                (emg_timestamps >= step_time - window_sec)
                & (emg_timestamps <= step_time + window_sec)
            )

            window_signal = emg_signal[mask]

            if window_signal.size == 0:
                aligned.append(
                    {
                        "step_time": float(step_time),
                        "emg_mean": 0.0,
                        "emg_rms": 0.0,
                        "emg_peak": 0.0,
                    }
                )
                continue

            aligned.append(
                {
                    "step_time": float(step_time),
                    "emg_mean": float(np.mean(window_signal)),
                    "emg_rms": float(np.sqrt(np.mean(window_signal ** 2))),
                    "emg_peak": float(np.max(np.abs(window_signal))),
                }
            )

        return aligned
