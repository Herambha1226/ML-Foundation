"""
17. Generate a sine wave using `np.linspace` and `np.sin`, then print first 10 values.

"""
import numpy as np 

arr = np.linspace(0,2*np.pi,100)
print(f" The linespace values: {arr[:10]}")

sine_wave = np.sin(arr)
print(f"The  Sine Wave values: {sine_wave[:10]}")

