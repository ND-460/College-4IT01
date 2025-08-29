print("By 22IT460")
num = int(input("Enter the number: "))
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
if isPrime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")