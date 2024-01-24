import numpy as np

A = np.array([1, 2, 3, 4])
print(A)
print(f"ndim = {np.ndim(A)}")
print(f"shape = {A.shape}")
print(f"shape[0] = {A.shape[0]}")

print("--------------")

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(f"ndim = {np.ndim(B)}")
print(f"shape = {B.shape}")