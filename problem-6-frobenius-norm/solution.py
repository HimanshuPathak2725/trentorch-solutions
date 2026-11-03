import numpy as np


def solve(A):
    # TODO: Return the Frobenius norm of A.
    return np.sqrt(np.sum(np.square(np.asarray(A))))
