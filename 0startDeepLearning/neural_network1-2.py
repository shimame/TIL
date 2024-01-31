import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(f"Z1_shape = {Z1.shape}")
print(f"W2_shape = {W2.shape}")
print(f"B2_shape = {B2.shape}")

A2 = np.dot(Z1, W2) + B2
print(f"A2 = {A2}")

Z2 = sigmoid(A2)
print(f"Z2 = {Z2}")