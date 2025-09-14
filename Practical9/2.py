print("By 22IT460")
file1 = input("Enter file name1: ")
file2 = input("Enter file name2: ")
file3 = input("Enter the file name for the merged results:")
with open(file3,"w") as mf:
    with open(file1,"r") as f1:
        mf.write(f1.read())
    with open(file2,"r") as f2:
        mf.write(f2.read())
digit_sum = 0
with open(file3,"r") as mf:
    content = mf.read()
    for x in content:
        if x.isdigit():
            digit_sum += int(x)
print(f"Content of merged file: {content}")
print(f"Sum of digits in content: {digit_sum}")