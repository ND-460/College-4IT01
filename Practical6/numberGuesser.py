import random
num = int(input("Enter the number between 1 to 6: "))
n = random.randint(1,6)
if num == n:
    print(f"You guessed it right, number is {n}")
else:
    print(f"You guessed it wrong, number was {n}")