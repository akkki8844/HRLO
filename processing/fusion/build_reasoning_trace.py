import numpy as np


class ReasoningTraceBuilder:
    def __init__(self):
        pass

    def build(
        self,
        step_timestamps,
        latencies,
        entropy,
        transitions,
        emg_aligned,
        coherence=None,
    ):
        step_timestamps = np.asarray(step_timestamps, dtype=float)
        latencies = np.asarray(latencies, dtype=float)
        entropy = np.asarray(entropy, dtype=float)

        trace = []

        for i in range(len(latencies)):
            step_trace = {
                "step_index": i + 1,
                "timestamp": float(step_timestamps[i + 1]),
                "latency": float(latencies[i]),
                "entropy": float(entropy[i]),
                "transition_strength": float(transitions[i])
                if i < len(transitions)
                else 0.0,
                "emg_mean": emg_aligned[i]["emg_mean"]
                if i < len(emg_aligned)
                else 0.0,
                "emg_rms": emg_aligned[i]["emg_rms"]
                if i < len(emg_aligned)
                else 0.0,
                "emg_peak": emg_aligned[i]["emg_peak"]
                if i < len(emg_aligned)
                else 0.0,
            }

            if coherence is not None and i < len(coherence):
                step_trace["coherence"] = float(coherence[i])

            trace.append(step_trace)

        return trace
