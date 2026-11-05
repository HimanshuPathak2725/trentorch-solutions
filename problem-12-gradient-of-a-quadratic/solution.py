import numpy as np


def solve(A, x, b):
    # TODO: Return the gradient 0.5*(A+A.T)@x + b.
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    x = np.asarray(x, dtype=float)

    return 0.5*(A + A.T)@x + b
