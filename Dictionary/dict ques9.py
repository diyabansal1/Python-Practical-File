# Write a program to get the maximum and minimum value of dictionary

d={}
size=int(input("enter size:"))
for i in range(size):
    k=eval(input("enter key:"))
    v=eval(input("enter value:"))
    d[k]=v
print(d)
val=d.values()
max=max(val)
min=min(val)
print(f'{max} is maximum')
print(f'{min} is minimum')