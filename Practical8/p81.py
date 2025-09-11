print("By 22IT460")
n1 = int(input("Enter the number 1"))
n2 = int(input("Enter the number 2"))
try:
    print(n1/n2)
    int("hello")
except ZeroDivisionError as e:
    print(f"Exception: {e}")
except ValueError as e:
    print(f"Exception: {e}")
