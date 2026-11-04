import numpy as np


def solve(x):
    """Implement Bernoulli Mean and Variance from the mathematical contract in README.md."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all((x == 0) | (x == 1)):
        raise ValueError("not good")
    mean = float(np.mean(x))

    return mean, mean * (1 - mean)
