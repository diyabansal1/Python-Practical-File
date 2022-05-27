# Write a program to displaying the size of a file after removing EOL characters, leading and trailing white spaces and blank lines.

file=open(r'E:\poem.txt',"r")
str1=""
size=0
tsize=0
while str1:
    str1=file.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("size of file after removing all EOL characters and blank lines:",size)
print("total size of file:",tsize)
file.close()