import numpy as np
from scipy.signal import butter, filtfilt


class EMGFilter:
    def __init__(
        self,
        low_cut_hz=20.0,
        high_cut_hz=450.0,
        notch_hz=50.0,
        fs=500,
        order=4,
    ):
        self.low_cut_hz = low_cut_hz
        self.high_cut_hz = high_cut_hz
        self.notch_hz = notch_hz
        self.fs = fs
        self.order = order

    def bandpass(self, signal):
        signal = np.asarray(signal, dtype=float)

        nyq = 0.5 * self.fs
        low = self.low_cut_hz / nyq
        high = self.high_cut_hz / nyq

        b, a = butter(self.order, [low, high], btype="band")
        return filtfilt(b, a, signal)

    def notch(self, signal, q=30.0):
        signal = np.asarray(signal, dtype=float)

        w0 = self.notch_hz / (0.5 * self.fs)
        b, a = butter(2, [w0 - w0 / q, w0 + w0 / q], btype="bandstop")
        return filtfilt(b, a, signal)

    def full_filter(self, signal):
        filtered = self.bandpass(signal)
        filtered = self.notch(filtered)
        return filtered
