# Write  a python program in which  function that accepts roll number and returns whether the student is present or absent.

def detail(roll):
    x = [23,43,22,56]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("enter roll no. :"))
detail(roll)