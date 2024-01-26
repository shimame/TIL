import numpy as np

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(f"W1_shape = {W1.shape}")
print(f"X_shape = {X.shape}")
print(f"B1_shape = {B1.shape}")

A1 = np.dot(X, W1) + B1
print(f"A1 = {A1}")