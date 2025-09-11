print("By 22IT460")
s1, s2 = "save", "vase"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
if len(s1) != len(s2):
    print("Not Anagram")
else:
    used = [False] * len(s2)
    is_anagram = True
    for ch1 in s1:
        found = False
        for i in range(len(s2)):
            if s2[i] == ch1 and not used[i]:
                used[i] = True
                found = True
                break
        if not found:
            is_anagram = False
            break
    print("Anagram" if is_anagram else "Not Anagram")
