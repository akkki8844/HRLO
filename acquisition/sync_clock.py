import time

class SyncClock:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def now(self):
        if self.start_time is None:
            raise RuntimeError("Clock has not been started")
        return time.perf_counter() - self.start_time