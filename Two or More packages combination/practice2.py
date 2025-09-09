""" 
Boolean Indexing with Conditions: Using the DataFrame from problem 1, filter it to show only the rows 
where the value in column 'A' is greater than the mean of column 'A' and the value in column 'B' is less 
than 50.
"""

import pandas as pd 
import numpy as np 

arr = np.random.randint(1,101,(10,3))
df = pd.DataFrame(arr)
df.rename(columns={0:"A"},inplace=True)
df.rename(columns={1:"B"},inplace=True)
df.rename(columns={2:"C"},inplace=True)
mean_col = df.mean(axis=0) 


row_high = df[df["A"]>mean_col["A"]]
print("The rows are shown below where the 'A' values are high to the mean of column 'A': \n",row_high)

col_low = df[df["B"]<50]
print("The column of 'B' where less than 50 that are shown below: \n",col_low)
 

