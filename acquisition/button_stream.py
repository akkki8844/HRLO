import serial
import threading
import time


class ButtonStream:
    """
    ButtonStream listens to a microcontroller (ESP32 / Arduino)
    that sends button press events over serial.

    Each button press represents the completion of one reasoning step.
    """

    def __init__(
        self,
        clock,
        port="/dev/ttyUSB0",
        baudrate=115200,
        timeout=1.0,
    ):
        self.clock = clock
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

        self.serial_conn = None
        self.thread = None
        self.running = False

        # Stored events: list of dicts
        self.events = []

    def connect(self):
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
            )
            time.sleep(2)  # allow serial to stabilize
            print(f"[ButtonStream] Connected to {self.port}")
        except serial.SerialException as e:
            raise RuntimeError(f"[ButtonStream] Serial connection failed: {e}")

    def start(self):
        if self.serial_conn is None:
            self.connect()

        self.running = True
        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()
        print("[ButtonStream] Listening for button events")

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)

        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

        print("[ButtonStream] Stopped")

    def _listen(self):
        """
        Expected serial message format from microcontroller:
        BUTTON,<button_id>
        Example:
        BUTTON,1
        """
        while self.running:
            try:
                line = self.serial_conn.readline().decode("utf-8").strip()
                if not line:
                    continue

                parts = line.split(",")
                if parts[0] != "BUTTON":
                    continue

                button_id = int(parts[1])
                timestamp = self.clock.now()

                event = {
                    "timestamp": timestamp,
                    "button_id": button_id,
                }

                self.events.append(event)
                print(f"[ButtonStream] Step {button_id} @ {timestamp:.6f}")

            except Exception as e:
                print(f"[ButtonStream] Warning: {e}")

    def get_events(self):
        """
        Returns a copy of all captured button events.
        """
        return list(self.events)

    def clear_events(self):
        """
        Clears stored events (used between trials).
        """
        self.events.clear()
