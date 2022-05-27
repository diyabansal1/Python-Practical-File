# Write a Python program to convert the list into nxm numpy array.

import numpy as np
r,c=list(map(int,input("enter rows and columns:").split()))
a=list(map(int,input("enter elements:").split()))
b=np.array(a).reshape(r,c)
print(b)