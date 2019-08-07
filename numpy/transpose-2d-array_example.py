import numpy as np

print("Original:")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

print("First way to transpose:")
print(np.transpose(a))

print("Second way to transpose:")
print(a.T)
