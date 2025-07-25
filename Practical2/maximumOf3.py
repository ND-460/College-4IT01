a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
if a >= b and a >= c:
    print(f"{a} is the maximum")
elif b >= c  and b >= a:
    print(f"{b} is the maximum")
else:
    print(f"{c} is  the maximum")