#  Program to handle multiple errors with one except statement.

 
def fun(a):
    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)
     
try:
    a=int(input("Enter the First Number: "))
    b=int(input("Enter the Second Number: "))
    fun(a)
    fun(b)
 
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")