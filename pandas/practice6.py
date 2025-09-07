""" 
6. Add a new column `marks` to the DataFrame, assigning values manually.
7. Sort students by `Marks` in descending order.
8. Find the **average marks per student** (row-wise mean).
9. Find the **maximum marks per subject** (column-wise max).

"""

import pandas as pd 


df = pd.read_csv("student_info.csv")
print("Normal Data Without any Filtering Data: ")

# Adding the New column of marks 
df['marks'] = [80,92,85,78,88,85,87,81,89,90]
print("New Column of Marks: \n",df)

# Now sort the data of students based on the marks 
modify = df.sort_values('marks')
print("Now Sort Data by using Marks: \n",modify)  # Note : These data only practice purpose that reason grades by Mistake grades are Wrong 

# Now find the Average marks of student with row wise
df["Avearage_marks"] = df.mean(axis=1,numeric_only=True)
print("Average Marks Row wise:\n")
print(df["Avearage_marks"])

# Now find the average marks of student with column wise 
df["Avearage_marks1"] = df.mean(axis =0,numeric_only=True) 
print("Average Marks Column Wise:\n")
print(df["Avearage_marks1"])
