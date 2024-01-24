import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
print(f"A_shape = {A.shape}")
B = np.array([7, 8])
print(f"B_shape = {B.shape}")
print(f"AB_dot = {np.dot(A, B)}")