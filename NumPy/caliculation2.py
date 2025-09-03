"""
Create a random 4×4 matrix, and find:

Maximum value

Minimum value

Index of the maximum value
"""
import numpy as np 

matrix = np.random.rand(4,4)
print(f"4x4 Matrix: {matrix}")

# now find Maximum Value
print(f"Maximum element value: {np.max(matrix)}")

# now find minumum value 
print(f"Minimum Element: {np.min(matrix)}")

# now find index of the macimum value
print(f"Index of the Maximum value: {np.argmax(matrix)}")
