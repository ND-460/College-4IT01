print("By 22IT460")
s1 = input("Enter the string1: ")
s2 = input("Enter the string2: ")
def endsWith(s1,s2):
    if len(s1) < len(s2):
        return False
    temp = s1[len(s1)-len(s2):len(s1)]
    for i in range(len(s2)):
        if temp[i] != s2[i]:
            return False
    return True
if endsWith(s1,s2):
    print(f"{s1} ends with {s2}")
else:
    print(f"{s1} does not ends with {s2}")