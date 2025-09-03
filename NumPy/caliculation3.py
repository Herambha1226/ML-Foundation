"""
Reshape a 1D array of 12 numbers into a 3×4 matrix.

Given two arrays:

a = np.array([1,2,3])
b = np.array([4,5,6])


Find:

Element-wise addition

Dot product

Cross product 
"""

import numpy as np

# Reshape 1D array into 3X4 
arr = np.array(np.random.randint(1,50,12))
print(f"12 Elements array: {arr}")

#reshape 
print(f"Reshape of Array: {arr.reshape(3,4)}")

# now perform operations on given arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

# Addition 
print(f" Element Wise Additon: {np.add(a,b)}")

# Dot Product
print(f"Element Dot Product: {np.dot(a,b)}")

#Cross Product 
print(f"Cross production: {np.cross(a,b)}")
