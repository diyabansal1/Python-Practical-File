# Write a NumPy program to create a NxM matrix, in which the elements on the borders will be equal to 1, and inside 0.

import numpy as np
r=int(input("enter rows:"))
c=int(input("enter columns:"))
x = np.ones((r,c))
x[1:-1, 1:-1] = 0
print(x)