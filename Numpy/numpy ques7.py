# Delete the second column from a given array and insert the following new column in its place.

import numpy

print("Printing Original array")
Array = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (Array)

print("Array after deleting column 2 on axis 1")
Array = numpy.delete(Array , 1, axis = 1) 
print (Array)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
Array = numpy.insert(Array , 1, arr, axis = 1) 
print (Array)