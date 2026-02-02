import numpy as np
import csv
import glob
import os


class RepeatabilityTest:
    def __init__(self):
        pass

    def load_latency_sessions(self, data_dir):
        sessions = []

        files = glob.glob(os.path.join(data_dir, "*_buttons_*.csv"))

        for path in files:
            timestamps = []
            with open(path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    timestamps.append(float(row["timestamp"]))

            if len(timestamps) >= 2:
                latencies = np.diff(timestamps)
                sessions.append(latencies)

        return sessions

    def compute_repeatability(self, sessions):
        if len(sessions) < 2:
            raise RuntimeError("At least two sessions required for repeatability test")

        means = np.array([np.mean(s) for s in sessions])
        stds = np.array([np.std(s) for s in sessions])

        coefficient_of_variation = stds / (means + 1e-9)

        return {
            "num_sessions": len(sessions),
            "mean_latency_mean": float(np.mean(means)),
            "std_latency_mean": float(np.std(means)),
            "mean_latency_std": float(np.mean(stds)),
            "std_latency_std": float(np.std(stds)),
            "mean_coefficient_of_variation": float(
                np.mean(coefficient_of_variation)
            ),
        }

    def run(self, data_dir):
        sessions = self.load_latency_sessions(data_dir)

        if len(sessions) < 2:
            raise RuntimeError("Insufficient data for repeatability analysis")

        return self.compute_repeatability(sessions)


if __name__ == "__main__":
    tester = RepeatabilityTest()
    results = tester.run("data/raw/button_events")

    print("Repeatability test complete")
    print(results)
