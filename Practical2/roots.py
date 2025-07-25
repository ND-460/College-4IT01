print("Enter the roots for following quadratic equations: ax^2+bx+c=0")
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))
d = pow(b,2) - 4 * a * c
c1 = (-b + pow(d,0.5))/(2 * a)
c2 = (-b - pow(d,0.5))/(2 * a)
print(f"roots of the equation are {c1} and {c2}")