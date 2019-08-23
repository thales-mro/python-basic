import numpy as np

data = np.random.randn(200, 400)
print("before operation:\n", data)
data[data > 0] = 0
print("after operation:\n", data)