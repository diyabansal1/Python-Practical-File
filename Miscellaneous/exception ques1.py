# Write a Program in Python to Manage Excepyions while Performing Arithmetic Operation on a User Input.

try:
    a=eval(input("Enter First number"))
    b=eval(input("Enter Second number"))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
except (NameError,ZeroDivisionError,ArithmeticError,TypeError):
    print("Exception Raised")