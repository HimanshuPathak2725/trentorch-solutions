import numpy as np

def solve(coeffs):
    """Solve the system a*x + b*y = e and c*x + d*y = f, where coeffs is [a,b,c,d,e,f]. A singular system raises ValueError."""
    x = np.asarray(coeffs)
    numX = coeffs[4]*coeffs[3] - coeffs[1]*coeffs[5]
    numY = coeffs[0]*coeffs[5] - coeffs[4]*coeffs[2]
    deno = coeffs[0]*coeffs[3] - coeffs[1]*coeffs[2]
    if deno == 0:
        raise ValueError("zero output")
    return np.asarray([numX, numY]) / deno
