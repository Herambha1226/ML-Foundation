"""
Generate an array of 100 random numbers and find:

Mean

Median

Variance

Standard deviation
"""
import numpy as np 

# generate array with 100 random numbers
arr = np.random.randint(1,753,100)
print(f"Array with 100 random numbers: {arr}")

# Mean 
print(f"Mean: {np.mean(arr)}")

# Medain 
print(f"Median: {np.median(arr)}")

# variance 
print(f"Varianace: {np.var(arr)}")

# Standard Deviation
print(f"Standard Deviation: {np.std(arr)}")
