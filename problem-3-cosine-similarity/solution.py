import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    x = np.dot(a, b)
    y, z = np.linalg.norm(a), np.linalg.norm(b)
    pro = np.dot(y, z)
    if x == 0 or y == 0:
        return 0.0
    return x / pro
