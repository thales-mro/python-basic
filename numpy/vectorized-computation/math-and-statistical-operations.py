import numpy as np

x = np.random.randn(5, 4)

print("Matrix:\n", x)

print("Mean:", x.mean())
print("Mean (using numpy):", np.mean(x))
print("Sum:", x.sum())
print("Mean (x-axis):", x.mean(axis=1))
print("Sum (y-axis):", x.sum(0))
