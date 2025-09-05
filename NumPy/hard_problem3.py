"""
15. Create a 5×5 random matrix and **normalize it** (all values between 0 and 1).

"""
"""
normalization: in numpy "normalize" typically refers to min-max scalling a process that scales an array's values 
to specific range ,usually formation.

formula: (data - data.min())/(data.max() - data.min())

"""


import numpy as np 


# creating the matrix
matrix = np.random.randint(0,50,(5,5))
print(f"5X5 Matrix with random numbers: {matrix}")

# now normalize applied the formula : (data - data.min())/(data.max() - data.min())
normalize = (matrix - matrix.min())/ (matrix.max() - matrix.min())
print(f"The values of Normalize matrix: {normalize}")
