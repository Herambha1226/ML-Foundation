""" 
5. Filter all rows where `grade > 3.0`.
"""
import pandas as pd 

df = pd.read_csv("student_info.csv")
rows = df.query("gpa > 3.0")
print(f"This output shows who are get gpa above 3.0: {rows}")
