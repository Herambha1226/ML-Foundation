""" 
3. Read a CSV file `students.csv` (create one if needed) and display:

   * First 5 rows (`head()`)
   * Number of rows & columns (`shape`)
   * Column names

"""
import pandas as pd 

df = pd.read_csv("student_info.csv")
top_5 = df.head()
shape = df.shape
col_names = df.columns
print(f"The First 5 rows: \n{top_5}")
print(f"The Shape of data: \n{shape}")
print(f"Data Column names: \n{col_names}")
