import time
import json
import numpy as np

from acquisition.sync_clock import SyncClock
from acquisition.emg_stream import EMGStream


class EMGCalibration:
    def __init__(
        self,
        duration_sec=20,
        port="/dev/ttyUSB0",
        sample_rate_hz=500,
    ):
        self.duration_sec = duration_sec
        self.port = port
        self.sample_rate_hz = sample_rate_hz

        self.clock = SyncClock()
        self.emg = EMGStream(
            clock=self.clock,
            port=self.port,
            sample_rate_hz=self.sample_rate_hz,
        )

    def run(self):
        print("EMG calibration started")
        print(f"Remain still for {self.duration_sec} seconds")

        self.clock.start()
        self.emg.start()

        time.sleep(self.duration_sec)

        self.emg.stop()

        samples = self.emg.get_samples()
        voltages = np.array([s["voltage"] for s in samples])

        if voltages.size == 0:
            raise RuntimeError("No EMG data captured during calibration")

        calibration = {
            "duration_sec": self.duration_sec,
            "sample_rate_hz": self.sample_rate_hz,
            "mean_voltage": float(np.mean(voltages)),
            "std_voltage": float(np.std(voltages)),
            "min_voltage": float(np.min(voltages)),
            "max_voltage": float(np.max(voltages)),
            "num_samples": int(voltages.size),
        }

        return calibration


if __name__ == "__main__":
    calibrator = EMGCalibration()
    calib_data = calibrator.run()

    with open("emg_calibration.json", "w") as f:
        json.dump(calib_data, f, indent=2)

    print("EMG calibration complete")
    print("Calibration data saved to emg_calibration.json")
