s = input("Enter the sentence: ")
upper = lower = number = 0
for i in range(len(s)) :
    if 'A' <= s[i] and s[i]  <= 'Z':
        upper += 1
    elif 'a' <= s[i] and s[i]  <= 'z':
        lower += 1
    elif not s[i].isspace():
        number += 1
print("Letters" ,upper+lower)
print("Upper" , upper)
print("Lower" , lower)
print("number" , number)