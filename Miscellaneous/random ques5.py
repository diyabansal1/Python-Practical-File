 # Write a Python Program to Generate Random Numbers from 1 to 100 and Append Them to the List.

import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,100))
print('Randomised list is: ',a)