print("By 22IT460")

try:
    filename = input("Enter the filename: ")
    with open(filename) as op:
        strs = op.read()
        op.close()
    # n1 = "Hello" + int(123)
    fhand = open(filename,"w")
except FileNotFoundError as e:
    print(f"Exception: {e}")

except PermissionError as e:
    print(f"Exception: {e}")

except TypeError as e:
    print(f"Exception: {e}")
