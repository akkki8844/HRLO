import threading
import time
import numpy as np
import mne

class EEGStream:
    def __init__(self, clock, sfreq=256, n_channels=4):
        self.clock = clock
        self.sfreq = sfreq
        self.n_channels = n_channels

        self.running = False
        self.thread = None

        self.samples = []

        self.info = mne.create_info(
            ch_names=[f"EEG{i}" for i in range(n_channels)],
            sfreq=sfreq,
            ch_types=["eeg"] * n_channels,
        )

    def start(self):
        self.runnung = True
        self.thread = threading.Thread(target=self._stream, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)

        def _stream(self):
            sample_interval = 1.0 / self.sfreq
            while self.running:
                timestamp = self.clock.now()
                sample = np.random.randn(self.n_channels)

                self.samples.append(
                    {
                        "timestamp": timestamp,
                        "values": sample,
                    }
                )

                time.sleep(sample_interval)

            def get_samples(self):
                return list(self.samples)
            
            def clear_samples(self):
                self.samples.clear()