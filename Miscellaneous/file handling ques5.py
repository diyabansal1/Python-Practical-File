# A text file contains alphanumeric text.Write a program that reads this text file and prints only the numbers or digits from the file.

f=open("an.txt","r")
for line in f:
    words=line.split()
    for i in words:
        for letter in i:
            if (letter.isdigit()):
                print(letter)