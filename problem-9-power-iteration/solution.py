import numpy as np


def solve(A, steps=100):
    # TODO: Return the dominant eigenvector via power iteration.
    A = np.asarray(A)
    v = np.ones(A.shape[1])
    v /= np.linalg.norm(v)
    for _ in range(steps):
        v = A @ v
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        v /= norm
        
    return v
