""" 
18. Create a **magic square checker**: Write a function that checks if a given 3×3 matrix is a magic square (sum of all rows, cols, diagonals same).

"""
import numpy as np 

def magic_matrix_checker(matrix):
    print(f"Given Matrix: {matrix}")
    
    index = 0
    rows = [] 
    for i, ele in enumerate(matrix):
        value = matrix[index,:]
        index+=1
        rows.append(value)
    value_row = np.sum(rows)
    index =0
    cols =[]
    for i in matrix:
        value = np.sum(matrix[:,index])
        index+=1
        cols.append(value)
    value_col = np.sum(cols)
    index1 = 0
    index2 = 0
    diagnols = []
    for i in matrix:
        diagn = matrix[index1,index2]
        diagnols.append(diagn)
        index1+=1
        index2+=1
    value_diagn1 = np.sum(diagnols) 
    
    index1 = len(matrix[0])-1
    index2 = len(matrix[0])-1
    diagnols2 = []
    for i in matrix:
        diagn = matrix[index1,index2]
        diagnols2.append(diagn)
        index1-=1
        index2-=1
    value_diagn2 = np.sum(diagnols2) 
    
    if value_col and value_row and value_diagn2 == value_diagn1:
        print("It's a Magic Matrix.")
    else: 
        print("It's not a Magic Matrix.")
            
matrix = np.array([[8,1,6],
                       [3,5,7],
                       [4,9,2]
                       ])
magic_matrix_checker(matrix)
