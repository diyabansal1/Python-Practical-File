# Write a program to compute height reached by the ladder on the wall for the given values of length and angle by user.

import math
length=float(input("enter length of ladder:"))
angle=float(input("enter angle of leaning(in degrees):"))
ang_radian=math.radians(angle)
heigth=length*math.sin(ang_radian)
print("ladder's height on the wall is:",heigth)