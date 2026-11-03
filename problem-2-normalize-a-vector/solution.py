import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    x = np.asarray(x, dtype=float)
    norm = np.sqrt(np.sum(np.square(x)))

    if norm == 0:
        raise ValueError("zero vector")

    return x / norm
