import os
import numpy as np
import matplotlib.pyplot as plt


class WaveformCompare:
    def __init__(self, output_dir="results/figures"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def compare(
        self,
        baseline_waveform,
        perturbed_waveform,
        title="Baseline vs Perturbed Reasoning Waveforms",
        filename="waveform_comparison.png",
    ):
        baseline_waveform = np.asarray(baseline_waveform, dtype=float)
        perturbed_waveform = np.asarray(perturbed_waveform, dtype=float)

        steps_base = np.arange(1, len(baseline_waveform) + 1)
        steps_pert = np.arange(1, len(perturbed_waveform) + 1)

        plt.figure(figsize=(9, 4))

        plt.plot(
            steps_base,
            baseline_waveform,
            marker="o",
            label="Baseline",
            linewidth=2,
        )

        plt.plot(
            steps_pert,
            perturbed_waveform,
            marker="o",
            linestyle="--",
            label="Perturbed",
            linewidth=2,
        )

        plt.xlabel("Reasoning Step")
        plt.ylabel("Latency (s)")
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path
