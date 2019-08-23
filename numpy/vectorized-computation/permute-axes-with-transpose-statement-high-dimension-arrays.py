import numpy as np

X = np.arange(16).reshape((2, 2, 4))
print("Original X:")
print(X)

Y = X.transpose((1, 0, 2))
print("Rearrange with transpose:")
print(Y)

print("Default transpose:")
print(X.T)