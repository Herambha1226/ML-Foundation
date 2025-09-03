"""Create a 6×6 matrix with 1 on the border and 0 inside (like a frame)"""
import numpy as np 

matrix = np.zeros((6,6),int)
matrix[0,:] = 1 
matrix[:,0] = 1
matrix[-1,:] = 1
matrix[:,-1] = 1
print(matrix)
