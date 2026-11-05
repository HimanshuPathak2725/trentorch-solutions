import numpy as np


def solve(f, x, h=1e-05):
    """Implement Finite Difference Derivative from the mathematical contract in README.md."""
    return float((f(x + h) - f(x - h)) / (2*h))
