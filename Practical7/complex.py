print("By 22IT460")
class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def display(self):
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {-self.imaginary}i")
c1= Complex(3,4)
c2 = Complex(5,6)
print("First complex: ", c1)
c1.display()
print("Second complex: ", c2)
c2.display()
c3 = c1 + c2
print("Third complex: ", c3)
c3.display()