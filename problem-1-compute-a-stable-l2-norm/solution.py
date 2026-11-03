import numpy as np

def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    x = np.asarray(x, dtype = float)
    maxi = np.max(np.abs(x))
    
    if maxi == 0:
        return 0.0
    scale = x / maxi
    norm = np.sqrt(np.sum(scale**2))

    return maxi * norm
