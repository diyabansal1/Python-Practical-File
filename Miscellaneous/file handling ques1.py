# Write a program to display the size of a file in bytes.

file=open(r'E:\poem.txt',"r")
str=file.read()
size=len(str)
print("size of the given file is:")
print(size,"bytes")