# Write a  function in python that accepts 3 values and returns the maximum of three numbers.


def max(a,b,c):
    if a>b and a>c:
        print(f'{a} is maximum among all')
    elif b>a and b>c:
        print(f'{b} is maximum among all')
    else:
        print(f'{c} is maximum among all')

s=int(input("enter 1st number:"))
p=int(input("enter 2nd number:"))
r=int(input("enter 3rd number:"))
max(s,p,r)

