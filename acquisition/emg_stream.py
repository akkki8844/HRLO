import threading
import time
import numpy as np
import serial


class EMGStream:
    def __init__(
        self,
        clock,
        port="/dev/ttyUSB0",
        baudrate=115200,
        sample_rate_hz=500,
        adc_max=4095,
        v_ref=3.3,
    ):
        self.clock = clock
        self.port = port
        self.baudrate = baudrate
        self.sample_rate_hz = sample_rate_hz
        self.adc_max = adc_max
        self.v_ref = v_ref

        self.serial_conn = None
        self.running = False
        self.thread = None

        self.samples = []

    def connect(self):
        self.serial_conn = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=1.0,
        )
        time.sleep(2)

    def start(self):
        if self.serial_conn is None:
            self.connect()

        self.running = True
        self.thread = threading.Thread(target=self._stream, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)

        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def _stream(self):
        sample_interval = 1.0 / self.sample_rate_hz

        while self.running:
            try:
                line = self.serial_conn.readline().decode("utf-8").strip()
                if not line:
                    continue

                if not line.startswith("EMG"):
                    continue

                _, raw_value = line.split(",")
                raw_value = int(raw_value)

                voltage = (raw_value / self.adc_max) * self.v_ref
                timestamp = self.clock.now()

                self.samples.append(
                    {
                        "timestamp": timestamp,
                        "raw": raw_value,
                        "voltage": voltage,
                    }
                )

                time.sleep(sample_interval)

            except Exception:
                continue

    def get_samples(self):
        return list(self.samples)

    def clear_samples(self):
        self.samples.clear()

    def get_signal_array(self):
        return np.array([s["voltage"] for s in self.samples])

    def get_timestamps(self):
        return np.array([s["timestamp"] for s in self.samples])
