# Low-Rank Reconstruction

Advanced | problemset | maths-stats-for-ml | svd

Reconstruct a matrix from only its first $k$ singular components (a truncated singular value decomposition).

Implement `solve(A, k)`.

**Returns.** Return a NumPy array of the same shape as `A`. The rank `k` is clipped into the valid range, and `k = 0` gives an all-zero matrix.

### Examples

**Example 1**

Input:

```python
solve([[3.0, 0.0], [0.0, 1.0]], 1)
```

Output:

```text
[[3.0, 0.0], [0.0, 0.0]]
```

**Example 2**

Input:

```python
solve([[1.0, 2.0], [3.0, 4.0]], 2)
```

Output:

```text
[[1.0, 2.0], [3.0, 4.0]]
```
