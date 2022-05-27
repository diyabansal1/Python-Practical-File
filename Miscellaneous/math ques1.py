# A triangle has three sides a,b,c. Calculate and display its area using heron's formula as s=a+b+c/2; area= (s*(s-a)*(s-b)*(s-c))**0.5

import math
a=int(input("enter first side:"))
b=int(input("enter second side:"))
c=int(input("enter third side:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("sides of triangle:",a,b,c)
print("area:",area,"units square")