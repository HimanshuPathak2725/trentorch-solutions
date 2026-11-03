import numpy as np

def solve(coeffs):
    """Solve the system a*x + b*y = e and c*x + d*y = f, where coeffs is [a,b,c,d,e,f]. A singular system raises ValueError."""
    a, b, c, d, e, f = coeffs
    det = a * d - b * c
    if det == 0:
        raise ValueError("singular system")
    return np.array([(e * d - b * f), (a * f - e * c)]) / det
