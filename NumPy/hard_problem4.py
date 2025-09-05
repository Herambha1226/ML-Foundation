""" 
16. Solve the system of linear equations using NumPy:

```
2x + y = 20
3x + 4y = 60
```
"""
import numpy as np

X = np.array([[2,1],
              [3,4]])
Y = np.array([20,60])

answer = np.linalg.solve(X,Y)

print(f"Solution of linear Equation: {answer}")
