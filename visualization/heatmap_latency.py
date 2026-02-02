import os
import numpy as np
import matplotlib.pyplot as plt


class LatencyHeatmap:
    def __init__(self, output_dir="results/figures"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate(
        self,
        latency_matrix,
        title="Latency Heatmap",
        xlabel="Reasoning Step",
        ylabel="Trial",
        filename="latency_heatmap.png",
    ):
        latency_matrix = np.asarray(latency_matrix, dtype=float)

        plt.figure(figsize=(8, 5))
        plt.imshow(latency_matrix, aspect="auto")
        plt.colorbar(label="Latency (s)")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()

        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()

        return path
