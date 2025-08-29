print("By 22IT460")
list1 = eval(input("Enter the list in form of {}: "))
def sumOfSquares(l):
    sum = 0
    for i in l:
        sum += (i * i)
    return sum
print(f"Sum of the {list1} is {sumOfSquares(list1)}")