# Gradient of a Quadratic

Advanced | problemset | maths-stats-for-ml | calculus

Return the gradient of the quadratic function $f(x)=\tfrac12 x^\top A x+b^\top x$. The matrix $A$ does not have to be symmetric.

Implement `solve(A, x, b)`.

**Returns.** Return a NumPy array of length $n$.

### Examples

**Example 1**

Input:

```python
solve([[2.0, 0.0], [0.0, 2.0]], [1.0, 1.0], [0.0, 0.0])
```

Output:

```text
[2.0, 2.0]
```

**Example 2**

Input:

```python
solve([[0.0, 1.0], [0.0, 0.0]], [1.0, 2.0], [0.0, 0.0])
```

Output:

```text
[1.0, 0.5]
```
