import numpy as np

array1d = np.arange(10)

print("Append example")
print("Original:")
print(array1d)
n_array1d = np.append(array1d, [4, 4, 4, 4])
print("After append:")
print(n_array1d)

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Append example (2D array)")
print("Original:")
print(array2d)
print("After append:")
n_array2d = np.append(array2d, [[99], [88], [77]], axis=1)
print(n_array2d)

print("Inserting element at specific index:")
print("Original:")
print(array1d)
print("After insert:")
print(np.insert(array1d, 1, 100))

print("Deleting specific value in array:")
print(np.delete(array1d, [1]))
