import numpy as np


class NoiseSensitivity:
    def __init__(self, noise_levels=None):
        if noise_levels is None:
            noise_levels = [0.01, 0.05, 0.1, 0.2]
        self.noise_levels = noise_levels

    def add_noise(self, signal, noise_level):
        signal = np.asarray(signal, dtype=float)
        noise = np.random.normal(0, noise_level * np.std(signal), size=signal.shape)
        return signal + noise

    def evaluate(self, signal, feature_fn):
        signal = np.asarray(signal, dtype=float)

        results = []

        for level in self.noise_levels:
            noisy_signal = self.add_noise(signal, level)
            feature_value = feature_fn(noisy_signal)

            results.append(
                {
                    "noise_level": level,
                    "feature_value": float(feature_value),
                }
            )

        return results


if __name__ == "__main__":
    def example_feature(x):
        return np.mean(np.abs(x))

    signal = np.random.randn(1000)

    analyzer = NoiseSensitivity()
    output = analyzer.evaluate(signal, example_feature)

    for r in output:
        print(r)
