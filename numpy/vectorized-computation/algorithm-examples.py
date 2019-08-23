import numpy as np

print("Inner product: X^T.X")
X = np.random.randn(6, 3)
print("X:", X)
Y = np.dot(X.T, X)
print("Y:", Y) 