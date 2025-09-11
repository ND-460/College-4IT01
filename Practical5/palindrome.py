print("By 22IT460")
s = "mom"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
i, j = 0, len(s) - 1
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
print("Palindrome" if is_palindrome else "Not Palindrome")
