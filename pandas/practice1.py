"""
1. Create a Pandas **Series** from a list `[10,20,30,40,50]`.

"""

import pandas as pd 

ls = [10,20,30,40,50]
pd.Series(ls)
df = pd.DataFrame(ls)
df.rename(columns={0:'Values'},inplace=True)
print(f"Data: \n {df}")
