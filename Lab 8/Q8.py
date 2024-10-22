import numpy as np

matrix1 = np.random.randint(1, 10, size=(5, 3))
matrix2 = np.random.randint(1, 10, size=(3, 2))

matrix = np.dot(matrix1, matrix2)

print("5x3 Matrix:")
print(matrix1)
print("\n3x2 Matrix:")
print(matrix2)
print("\nResultant matrix after Multiplication:")#5x2 matrix
print(matrix)
