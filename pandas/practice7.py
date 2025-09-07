""" 
10. Replace missing values (`NaN`) in `Average` with the average marks.
11. Count how many students got each `Grade` (`value_counts`).
12. Rename column `Average` → `Score`.
13. Drop the column `Age` from the DataFrame.

"""

import pandas as pd 
import numpy as np 
df = pd.read_csv("student_info.csv")
print("This is original data: \n",df)

# Now add one column of Average with NaN data 
df["Average"] = np.nan
print(df)

# Count Equal Numbers 
Count = df["grade"].value_counts()
print(Count) 

# rename the column name average into score 
rename = df.rename(columns={"Average":"Score"})
print(rename)


# drop the column of Age 
drop = df.drop(["age"],axis=1,inplace=True)
print(df)
