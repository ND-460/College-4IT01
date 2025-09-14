from collections import Counter
print("By 22IT460")
filename = input("Enter file name: ")
with open(filename,"r") as f:
    content = f.read()
    f.close()
letters = [ch.lower() for ch in content if ch.isalpha()]
freq = Counter(letters)
print(freq)
for letter,count in freq.items():
    print(f"{letter}: {"*" * count}")