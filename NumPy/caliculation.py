"""
Given arr = np.array([1,2,3,4,5]), calculate:

Square of each element

Sum of all elements

Standard deviation
"""
import numpy as np 

arr = np.array([1,2,3,4,5])
index = 0
#now find the square root each element
print(f"Squre of each element: {arr**2}")

# now find Sum of All Elements
print(f"Sum Of All Elements: {np.sum(arr)}")

# standard deviation 
print(f"Stardard Deviation: {np.std(arr)}")
