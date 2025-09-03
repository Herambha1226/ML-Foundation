#   Convert this Python list [1,2,3,4,5] into a NumPy array and find its mean and sum

import numpy as np

ls = [1,2,3,4,5]
cvt_arr = np.array(ls)
print(f"Python List Converts into Array : {cvt_arr}")

# Now i find the mean and sum 
print(f"Mean of array: {np.mean(cvt_arr)}")
print(f"Sum of Converted Array: {np.sum(cvt_arr)}")

