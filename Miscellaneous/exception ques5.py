# Program to Print the Cube of Even Numbers.


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    r=(num**3)
    print(r)