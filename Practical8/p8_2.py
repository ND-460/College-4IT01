print("By 22IT460")
class MyCustomException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message}"
n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
try:
    if(n2 == 0):
        raise MyCustomException(f"Denominator is zero")
except MyCustomException as e:
    print(f"Exception: {e}")