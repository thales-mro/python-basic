import numpy as np

A = np.array([[0.84, -0.26, 0.92], [0.42, 0.31, -0.73]])
print("A array:")
print(A)

print("Setting all the negative values of A to zero:")
A[A < 0] = 0
print(A)
