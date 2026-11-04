import numpy as np


def solve(f, samples):
    # TODO: Return the mean of f applied to the samples.
    smaples = np.asarray(samples, dtype=float)
    return float(np.mean((f(samples))))
