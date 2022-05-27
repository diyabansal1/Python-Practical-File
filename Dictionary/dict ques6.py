# Program to find list of all possible combinations of letters of a given string s in Python

st_arr = []
s=input("enter string:")
for i in range(len(s)-1,-1,-1):
    for j in range(len(st_arr)):
        st_arr.append(s[i]+st_arr[j])
    st_arr.append(s[i])
   


print(st_arr)