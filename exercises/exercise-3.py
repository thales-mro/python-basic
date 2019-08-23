import numpy as np

a = np.array([1, 2, 3, 4, 5])

print("Before reversion\n", a)

b = a[::-1]

print("After reversion:\n", b, "\nor")

print(np.flipud(a))