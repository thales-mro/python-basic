import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Examples:")
print("A:")
print(a)
print("B:")
print(b)

print("Common matrix product:")
x = np.dot(a, b)
print(x)

print("Element-wise multiplication (Hadamard product):")
y = np.multiply(a, b)
print(y)

print("Element-wise multiplication (Hadamard product) (another notation):")
z = a * b
print(z)
