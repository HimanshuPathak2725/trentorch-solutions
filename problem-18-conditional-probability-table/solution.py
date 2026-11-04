import numpy as np


def solve(A, B):
    # TODO: Return P(A|B) = sum(A & B) / sum(B), or 0.0 when sum(B) is 0.
    A, B = np.asarray(A, dtype=bool), np.asarray(B, dtype=bool)

    if np.sum(B) == 0:
        return 0.0

    return float(np.sum(A & B) / np.sum(B))
