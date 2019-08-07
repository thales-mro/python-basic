import numpy as np

print("Creating array based on a range:")
array1d = np.arange(10)
print(array1d)

print("Getting slice of array:")
print(array1d[5:8])

print("Manipulating slice of array:")
array1d[5:8] = 99
print(array1d)

print("Let's manipulate the following 2d array:")
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(array2d)

print("Getting slice in the row level:")
print(array2d[:2])

print("Getting slice in the row level, specific column:")
print(array2d[0:2, 1])

print("Getting slice in both row and column levels:")
print(array2d[:2, 1:])

print("Even more sophisticated slice:")
print(array2d[1:5:2, ::3])

print("select values from array that fulfill certain condition")
a = np.random.random((1, 7))
print("Original:")
print(a)
print("Condition:")
print(a[a < 0.6])
