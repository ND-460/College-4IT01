print("By 22IT460")
filename = input("Enter file name to create: ")
print("Enter the string to enter(end the input with #): ")

with open(filename, "w") as file:
    while True:
        line = input()
        if line.strip() == "#":
            break
        file.write(line+"\n")
lines = 0
spaces = 0

with open(filename, "r") as file:
    for line in file:
        lines += 1
        spaces += line.count(" ")
print(f"Total lines: {lines} and total spaces: {spaces}")