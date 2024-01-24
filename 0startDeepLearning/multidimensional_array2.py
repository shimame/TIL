import numpy as np

A1 = np.array([[1, 2], [3, 4]])
print(A1)
print(f"A1_shape = {A1.shape}")

print("------------------")

B1 = np.array([[5, 6], [7, 8]])
print(B1)
print(f"B1_shape = {B1.shape}")

print(f"A1B1_dot = {np.dot(A1, B1)}")

print("------------------")

A2 = np.array([[1, 2, 3], [4, 5, 6]])
print(A2)
print(f"A2_shape = {A2.shape}")

print("------------------")

B2 = np.array([[1, 2], [3, 4], [5, 6]])
print(B2)
print(f"B2_shape = {B2.shape}")

print(f"A2B2_dot = {np.dot(A2, B2)}")