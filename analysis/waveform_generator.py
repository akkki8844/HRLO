import numpy as np

class WaveformGenerator:
    def __init__(self, smoothing_window=3):
        self.smoothing_window = smoothing_window   
    
    def generate(self, step_timestamps):
        step_timestamps = np.asarray(step_timestamps, dtype=float)

        if step_timestamps.size < 2:
            return {
                "latencies": [],
                "waveform": [],
            }
        
        latencies = np.diff(step_timestamps)
        waveform = self._smooth(latencies)

        return {
            "latencies": latencies.tolist(),
            "waveform": waveform.tolist(),
        }
    
    def _smooth(self, x):
        if x.size < self.smoothing_window:
            return x
        
        kernel = np.ones(self.smoothing_window) / self.smoothing_window
        return np.convolve(x, kernel, mode="same")