print("By 22IT460")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
dict1 = dict()
dict1[num] = factorial(num)
print(f"The factorial of {num} is {dict1[num]}")
print(f"Stored dictionary: {dict1}")