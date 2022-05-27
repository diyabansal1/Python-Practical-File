# Write a program to input the radius of a sphere and calculate its volume.

import math

r = float(input("Enter radius of sphere: "))
v = 4 / 3 * math.pi * r ** 3

print("Volume of sphere = ", v)