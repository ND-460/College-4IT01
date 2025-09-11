print("By 22IT460")
s = "Coding"
print("Reversed:", s[::-1])
rev = ""
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
print("Reversed (without inbuilt):", rev)
