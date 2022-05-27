# Write a program to generate 6 random numbers and then print their mean, median and mode.

import random
import statistics

a = random.random()
b = random.random()
c = random.random()
d = random.random()
e = random.random()
f = random.random()

print("Generated Numbers:")
print(a, b, c, d, e, f)

seq = (a, b, c, d, e, f)

mean = statistics.mean(seq)
median = statistics.median(seq)
mode = statistics.mode(seq)

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)