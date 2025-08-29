print("By 22IT460")
list1 = eval(input("Enter the list in form of {}: "))
def product(l):
    prod = 1
    for i in l:
        prod *= i
    return prod
print(f"The product of {list1} is {product(list1)}")