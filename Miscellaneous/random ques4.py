# Write a program to generate arandom floating number between 45.0 and 95.0. Print this number along with its nearest integer greater than it.

import random
import math
fnum=random.random()*(95-45)+45
inum=math.ceil(fnum)
print("random numbers are:",fnum)
print("nearest highest integer:",inum)