""" 
4. Select the `Age` column from a DataFrame.

"""
import pandas as pd 

df = pd.read_csv("student_info.csv")
col = df['age']
print(f"This data comes from Selecting column: {col.to_list()}")
