import numpy as np

# creating a 1D array 
numbers = np.random.randint(1,100,20)
OneD = np.array(numbers)
print(f"First Array: {OneD}")

numbers2 = np.random.randint(100,200,20)
TwoD = np.array(numbers2)
print(f"Seccond Array: {TwoD}")

# Simple Mathematical operations
Addition = np.add(OneD,TwoD)
print(f"Addition: {Addition}")

Multiply = np.multiply(OneD,TwoD)
print(f"Multiply: {Multiply}")

Division = np.divide(OneD,TwoD)
print(f"Division: {Division}")

Subtract = np.subtract(OneD,TwoD)
print(f"Subtraction: {Subtract}")
