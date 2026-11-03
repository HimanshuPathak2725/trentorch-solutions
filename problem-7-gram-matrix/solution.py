import numpy as np


def solve(X):
    # TODO: Return the Gram matrix X^T X.
    X = np.asarray(X, dtype=float)
    return (np.transpose(X) @ X)
