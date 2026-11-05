import numpy as np


def solve(f, x, h=1e-05):
    """Implement Jacobian by Finite Differences from the mathematical contract in README.md."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(f(x), dtype=float)
    J = np.zeros((len(y), len(x)))
    for j in range(len(x)):
        e = np.zeros_like(x)
        e[j] = h
        J[:, j] = (np.asarray(f(x + e)) - np.asarray(f(x - e))) / (2 * h)
    return J
