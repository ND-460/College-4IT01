import re
print("By 22IT460")
filename = input("Enter the filename to load the records: ")
with open(filename, "r") as f:
    lines = f.readlines()
result = input("Enter the filename for the result: ")
with open(result, "w") as f:
    for line in lines:
        if re.search("388120", line):
            print(line, end='')
            f.write(line)
result1 = input("Enter the filename to store updated results")
with open(result,"r") as f:
    content = f.readlines()
with open(result1,"w") as f:
    for lines in content:
        temp = re.sub("388120","388325",lines)
        print(temp, end='')
        f.write(temp)
