import numpy as np
import matplotlib.pyplot as plt
import time


class OscilloscopeView:
    def __init__(self, refresh_rate_hz=10):
        self.refresh_rate_hz = refresh_rate_hz
        self.last_update = time.time()

        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.line, = self.ax.plot([], [], lw=2)

        self.ax.set_xlabel("Reasoning Step")
        self.ax.set_ylabel("Latency / Signal Amplitude")
        self.ax.set_title("Reasoning Oscilloscope View")
        self.ax.grid(True)

    def update(self, signal, collapse_step=None):
        current_time = time.time()
        if current_time - self.last_update < 1.0 / self.refresh_rate_hz:
            return

        signal = np.asarray(signal, dtype=float)

        self.line.set_xdata(np.arange(1, len(signal) + 1))
        self.line.set_ydata(signal)

        self.ax.relim()
        self.ax.autoscale_view()

        if collapse_step is not None:
            self.ax.axvline(
                x=collapse_step + 1,
                linestyle="--",
                linewidth=2,
            )

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.last_update = current_time

    def close(self):
        plt.ioff()
        plt.close(self.fig)
