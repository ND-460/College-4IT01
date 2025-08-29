print("By 22IT460")
s = input("Enter the string: ")
def totalUpperAndLower(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
    return lower,upper
totalLower,totalUpper = totalUpperAndLower(s)
print(f"Total lower in {s} is {totalLower}\nTotal upper in {s} is {totalUpper}")
