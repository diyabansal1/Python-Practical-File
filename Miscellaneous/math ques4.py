# Python program to calculate the area of an equilateral triangle.

import math 


s=int(input("enter side:"))

a = (math.sqrt(3) / 4) * (s * s)
print("Area of the equilateral triangle = ", a, " sq. units")
