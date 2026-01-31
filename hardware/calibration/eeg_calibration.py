import numpy as np
import time
import json

from acquisition.eeg_stream import EEGStream
from acquisition.sync_clock import SyncClock


class EEGCalibration:
    def __init__(self, duration_sec=30, sfreq=256):
        self.duration_sec = duration_sec
        self.sfreq = sfreq
        self.clock = SyncClock()
        self.eeg = EEGStream(self.clock, sfreq=sfreq)

    def run(self):
        self.clock.start()
        self.eeg.start()

        print("EEG calibration started")
        print(f"Remain still for {self.duration_sec} seconds")

        time.sleep(self.duration_sec)

        self.eeg.stop()
        samples = self.eeg.get_samples()

        values = np.array([s["values"] for s in samples])

        mean = np.mean(values, axis=0).tolist()
        std = np.std(values, axis=0).tolist()

        calibration = {
            "sampling_rate_hz": self.sfreq,
            "duration_sec": self.duration_sec,
            "channel_mean": mean,
            "channel_std": std,
        }

        return calibration


if __name__ == "__main__":
    calibrator = EEGCalibration()
    calib_data = calibrator.run()

    with open("eeg_calibration.json", "w") as f:
        json.dump(calib_data, f, indent=2)

    print("EEG calibration complete")
    print("Calibration data saved to eeg_calibration.json")
