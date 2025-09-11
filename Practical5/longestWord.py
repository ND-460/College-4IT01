print("By 22IT460")
sentence = "Theory makes coding interesting"
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)
longest = ""
word = ""
for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
print("Longest word (without any inbuilt):", longest)
