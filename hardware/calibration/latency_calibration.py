import time
import json
import statistics

from acquisition.sync_clock import SyncClock


class LatencyCalibration:
    def __init__(self, trials=20):
        self.trials = trials
        self.clock = SyncClock()
        self.latencies = []

    def run(self):
        print("Latency calibration started")
        print("Press ENTER as fast as possible when prompted")

        self.clock.start()

        for i in range(self.trials):
            time.sleep(1.0)
            print(f"Trial {i + 1}: PRESS ENTER NOW")
            t_start = self.clock.now()
            input()
            t_end = self.clock.now()
            self.latencies.append(t_end - t_start)

        calibration = {
            "trials": self.trials,
            "mean_reaction_time_sec": statistics.mean(self.latencies),
            "median_reaction_time_sec": statistics.median(self.latencies),
            "std_reaction_time_sec": statistics.stdev(self.latencies)
            if len(self.latencies) > 1
            else 0.0,
            "all_latencies_sec": self.latencies,
        }

        return calibration


if __name__ == "__main__":
    calibrator = LatencyCalibration()
    data = calibrator.run()

    with open("latency_calibration.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Latency calibration complete")
    print("Calibration data saved to latency_calibration.json")
