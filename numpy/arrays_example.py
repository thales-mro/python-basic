import numpy as np

print("Creating array of zeros")
a = np.zeros(shape=(3, 2))
print(a)

print("Setting elements in array:")
a[0] = [1, 2]
a[1] = [3, 4]
a[2][0] = 9
print(a)

print("Creating array of ones:")
x = np.ones((3, 4))
print(x)
print("Checking the shape of an array:")
print(x.shape)

print("Creating array of zeros, setting elements' type:")
t = np.zeros((2, 3, 4), dtype = np.int16)
print(t)

print("Creating array with random values:")
r = np.random.random((2, 2))
print(r)

print("Creating array with constant as initial value to elements:")
c = np.full((2, 2), 7)
print(c)

print("Create array of evenly-spaced values (last param is the step size):")
e = np.arange(10, 25, 5)
print(e)

print("Create another array of evenly-spaced values (last param is the size of array):")
e2 = np.linspace(0, 2, 9)
print(e2)
