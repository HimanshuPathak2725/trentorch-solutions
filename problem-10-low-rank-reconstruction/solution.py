import numpy as np

def solve(A, k):
    """Reconstruct A from its first k singular components using a truncated singular value decomposition."""
    np.asarray(A, dtype=float)
    U, S, VT = np.linalg.svd(A, full_matrices=False)

    A_k = U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

    return A_k
