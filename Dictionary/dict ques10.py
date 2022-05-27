# Write a python program to find that if values are exist in dictionary or not.

d={}
size=int(input("enter size:"))
for i in range(size):
    k=eval(input("enter key:"))
    v=eval(input("enter value:"))
    d[k]=v
print(d)
val=d.values()
k1=eval(input("enter value to find if exist:"))
if k1 in val:
    print("value exists in a dictionary")
else:
    print("value not exists in a dictionary")