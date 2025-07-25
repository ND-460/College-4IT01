num = int(input("Enter the number: "))
n = num
sum = 0
while n > 0:
    sum += (n % 10)
    n = n // 10
print(f"The sum of digit in {num} is {sum}")