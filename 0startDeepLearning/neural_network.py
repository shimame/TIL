import numpy as np

X = np.array([1, 2])
print(f"X_shape = {X.shape}")
W = np.array([[1, 3, 5], [2, 4, 6]])
print(f"W_shape = {W.shape}")
print(f"XW_dot = {np.dot(X, W)}")