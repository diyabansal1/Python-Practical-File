# Write a program to read a text file line by line and display each word separated by a '#'.

file=open("Answer.txt","r")
line=" "
while line:
    line=file.readline()
    for word in line.split():
        print(word,end="#")
    print()
    file.close()