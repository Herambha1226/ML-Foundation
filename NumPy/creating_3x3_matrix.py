import numpy as np

#creating 3x3 matrix
matrix1 = np.random.randint(1,20,(3,3))
print(f"3x3 Matrix1: {matrix1}")

matrix2 = np.random.randint(21,40,(3,3))
print(f"3x3 Matrix2: {matrix2}")

# some normal operations are below

print(f"Addition: {np.add(matrix1,matrix2)}\n")
print(f"Subtration: {np.subtract(matrix1,matrix2)}\n")
print(f"Multiplication: {np.multiply(matrix1,matrix2)}\n")
print(f"Division: {np.divide(matrix1,matrix2)}\n")

# some Statistics Operations on each matrix
print(f"Sum of all Elements: {np.sum(matrix1)}\n")
print(f"Mean/Average of Matrix2: {np.mean(matrix2)}\n")
print(f"Median of Matrix1: {np.median(matrix1)}\n")
print(f"Maximum number Index In MAtrix1: {np.argmax(matrix2)}\n")


