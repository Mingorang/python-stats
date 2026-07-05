import numpy as np
from scipy.linalg import solve

size = int(input("What is the size of the simultaneous equation? (2-4): "))
if size == 2:
    print("Matrix A will be a 2 x 1 matrix, so matrix b will have 2 variables x and y.")
elif size == 3:
    print("Matrix A will be a 3 x 1 matrix, so matrix b will have 3 variables x, y and z.")
elif size == 3:
    print("Matrix A will be a 4 x 1 matrix, so matrix b will have 4 variables x, y, z and t.")
#Eqauations are of form Ax=b
A = []
b = []

#Finding matrix A (coefficient matrix)
for i in range(size):
    row = []
    for j in range(size):
        coefficient = float(input("Coefficient at specific point: "))
        row.append(coefficient)
    A.append(row)
A = np.array(A)
print(A)
