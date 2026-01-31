import numpy as np
from scipy import stats

class Statistics:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def describe(self, data):
        data = np.asarray(data, dtype=float)
        return {
            "mean": float(np.mean(data)),
            "median": float(np.median(data)),
            "std": float(np.std(data)) if data.size > 1 else 0.0,
            "min": float(np.min(data)),
            "max": float(np.max(data)),
            "count": int(len(data)),
        }
    
    def compare_conditions(self, a, b):
        a = np.asarray(a, dtype=float)
        b = np.asarray(b, dtype=float)

        if a.size < 2 or b.size < 2:
            return None
        
        pooled_std = np.sqrt(
            ((np.var(a, ddof=1) + np.var(b, ddof=1)) / 2)
        )
        if pooled_std == 0:
            return 0.0
        
        return float((np.mean(a) - np.mean(b)) / pooled_std)