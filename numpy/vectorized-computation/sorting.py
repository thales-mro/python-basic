import numpy as np

x = np.random.randn(6)
print("Before sorting: ", x)

x.sort()
print("After sorting (in-place): ", x)