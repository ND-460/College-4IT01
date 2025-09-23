import re
print("By 22IT460")
filename = input("Enter the file to open: ")
with open(filename, "r") as f:
    lines = f.readlines()
    f.close()
print(lines)
result = input("Enter the file to store the results: ")
with open(result, "w") as f:
    for line in lines:
        words = line.split(",")
        if re.search(r"^[RSrs].*[HJhj]$", words[0]):
            f.write(line)

with open(result, "r") as f:
    content = f.read()
    f.close()
print("\nMatched lines:")
print(content)
