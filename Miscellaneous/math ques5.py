# Write a program to find a side of a right angled triangle whose two sides and an angle is given.

import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))
ang = float(input("Enter angle(in degrees): "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)