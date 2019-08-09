import numpy as np

a = np.array([[0, 1], [2, 3]])
print("Original Array:")
print(a)
print("Resize example:")
print(np.resize(a, (2, 3)))

print("Reshape example: (size of array should be unchanged)")
print("Original:")
x = np.ones((3, 4))
print(x)
print("Size:", x.size)
y = x.reshape((2, 6))
print("After reshape:")
print(y)
        
print("Ravel transforms n-D arrays to 1-D array:")
z = x.ravel()
print(z)
