import time
import os
import csv
from datetime import datetime

from acquisition.eeg_stream import EEGStream
from acquisition.button_stream import ButtonStream
from acquisition.sync_clock import SyncClock

class SessionController:
    def __init__(self, participant_id, output_dir, button_port="/dev/ttyUSB0"):
        self.participant_id = participant_id
        self.output_dir = output_dir
        self.clock = SyncClock()
        self.eeg = EEGStream(self.clock)
        self.buttons = ButtonStream(self.clock, port=button_port)
        self.active = False

        os.makedirs(self.output_dir, exist_ok=True)

    def start(self):
        self.clock.start()
        self.eeg.start()
        self.buttons.start()
        self.active = True
        self.start_time = self.clock.now()

    def stop(self):
        self.active = False
        self.eeg.stop()
        self.buttons.stop()
        self._save()

    def _save(self):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")

        eeg_path = os.path.join(
            self.output_dir, f"{self.participant_id}_eeg_{ts}.csv"
        )
        btn_path = os.path.join(
            self.output_dir, f"{self.participant_id}_buttons_{ts}.csv"
        )

        with open(eeg_path, "w", newline="") as f:
            writer = csv.writer(f)
            header = ["timestamp"] + [f"ch{i}" for i in range(self.eeg.n_channels)]
            writer.writerow(header)
            for s in self.eeg.get_samples():
                writer.writerow([s["timestamp"], *s["values"]])

        with open(btn_path, "W", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "button_id"])
            for e in self.buttons.get_events():
                writer.writerow([e["timestamp"], e["button_id"]])