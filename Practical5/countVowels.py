print("By 22IT460")
s = "Good Morning"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count)
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    for v in vowels:
        if ch == v:
            count += 1
print("Vowel count (without inbuilt function):", count)
