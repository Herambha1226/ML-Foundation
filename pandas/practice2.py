"""
2. Create a **DataFrame** with 2 columns (`Name`, `Age`) and 3 rows.

"""
import pandas as pd 

data = {
    'Name':['Herambha','Karthikeya','Guptha'],
    'Age': [17,19,21]
}
pd.Series(data)
df = pd.DataFrame(data)

print(f"Data: \n {df}")
