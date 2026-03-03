import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

def matrix_addition(A, B):
    return A + B

def dot_product(A, B):
    return np.dot(A, B)


print("Matrix Addition", matrix_addition(A, B))
print("Dot Product:", dot_product(A, B))