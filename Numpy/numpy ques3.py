# Write a NumPy program to sort a given array by row and column in ascending order.

import numpy as np  
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 4.38, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
print("\nSort the said array by row in ascending order:")
print(np.sort(nums))
print("\nSort the said array by column in ascending order:")
print(np.sort(nums, axis=0))