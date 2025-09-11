print("By 22IT460")
s = "   Thank God   "
print("Before:", repr(s))
print("After :", repr(s.strip()))
i, j = 0, len(s) - 1
while i < len(s) and s[i] == " ":
    i += 1
while j >= 0 and s[j] == " ":
    j -= 1
trimmed = ""
for k in range(i, j + 1):
    trimmed += s[k]
print("After (without inbuilt):", repr(trimmed))
