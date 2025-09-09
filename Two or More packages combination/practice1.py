""" 
DataFrame from NumPy Array: Create a 10x3 NumPy array of random integers between 1 and 100. 
Convert this array into a Pandas DataFrame with the columns ['A', 'B', 'C']. Then, calculate the mean of 
each column.
"""

import pandas as pd 
import numpy as np 

arr = np.random.randint(1,101,(10,3))
print(f"10x3 array with 1 to 100 random numbers:\n {arr}")

df = pd.DataFrame(arr)
df.rename(columns={0:"A"},inplace=True)
df.rename(columns={1:"B"},inplace=True)
df.rename(columns={2:"C"},inplace=True)
print(f"The array converted into padas dataframe: \n {df}")

mean_col = df.mean(axis=0) 
print("The mean is given below as column wise: \n",mean_col)



