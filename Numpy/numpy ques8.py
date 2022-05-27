# You are given a space separated list of numbers.
#  Write a python program to print a reversed Numpy array with the element type float.

import numpy as np
a=list(map(float,input("enter elements:").split()))
b=np.array(a)
b=np.array(a[: : -1])
print(b)