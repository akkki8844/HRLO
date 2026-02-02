import os
import matplotlib.pyplot as plt
import numpy as np


class FigureExporter:
    def __init__(self, output_dir="results/figures"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_latency_waveform(self, latencies, title="Latency Waveform", filename="latency_waveform.png"):
        latencies = np.asarray(latencies, dtype=float)

        plt.figure(figsize=(8, 4))
        plt.plot(range(1, len(latencies) + 1), latencies, marker="o")
        plt.xlabel("Reasoning Step")
        plt.ylabel("Latency (s)")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path

    def save_entropy_curve(self, entropy, title="Latency Entropy", filename="latency_entropy.png"):
        entropy = np.asarray(entropy, dtype=float)

        plt.figure(figsize=(8, 4))
        plt.plot(range(1, len(entropy) + 1), entropy, marker="o")
        plt.xlabel("Reasoning Step")
        plt.ylabel("Entropy")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path

    def save_emg_alignment(self, emg_aligned, title="EMG Aligned to Reasoning Steps", filename="emg_alignment.png"):
        steps = []
        rms_values = []

        for i, e in enumerate(emg_aligned, start=1):
            steps.append(i)
            rms_values.append(e["emg_rms"])

        plt.figure(figsize=(8, 4))
        plt.bar(steps, rms_values)
        plt.xlabel("Reasoning Step")
        plt.ylabel("EMG RMS")
        plt.title(title)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path

    def save_collapse_marker(
        self,
        latencies,
        collapse_step,
        title="Collapse Detection",
        filename="collapse_detection.png",
    ):
        latencies = np.asarray(latencies, dtype=float)

        plt.figure(figsize=(8, 4))
        plt.plot(range(1, len(latencies) + 1), latencies, marker="o")

        if collapse_step is not None:
            plt.axvline(
                x=collapse_step + 1,
                linestyle="--",
                linewidth=2,
            )

        plt.xlabel("Reasoning Step")
        plt.ylabel("Latency (s)")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path
