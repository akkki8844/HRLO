import numpy as np
import csv
import glob
import os


class HardwareVariance:
    def __init__(self):
        pass

    def load_emg_sessions(self, data_dir):
        sessions = []

        files = glob.glob(os.path.join(data_dir, "*_emg_*.csv"))

        for path in files:
            voltages = []
            with open(path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    voltages.append(float(row["voltage"]))

            if len(voltages) > 0:
                sessions.append(np.array(voltages))

        return sessions

    def compute_variance(self, sessions):
        if len(sessions) < 2:
            return None

        means = np.array([np.mean(s) for s in sessions])
        stds = np.array([np.std(s) for s in sessions])

        return {
            "mean_of_means": float(np.mean(means)),
            "std_of_means": float(np.std(means)),
            "mean_of_stds": float(np.mean(stds)),
            "std_of_stds": float(np.std(stds)),
            "num_sessions": len(sessions),
        }

    def analyze(self, data_dir):
        sessions = self.load_emg_sessions(data_dir)

        if len(sessions) < 2:
            raise RuntimeError("Insufficient sessions for hardware variance analysis")

        return self.compute_variance(sessions)


if __name__ == "__main__":
    analyzer = HardwareVariance()
    results = analyzer.analyze("data/raw/emg")

    print("Hardware variance analysis complete")
    print(results)
