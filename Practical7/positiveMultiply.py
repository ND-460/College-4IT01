print("By 22IT460")
class Number:
    def __init__(self, num):
        self.num = num
class PositiveNumber:
    def getPositive(self, num):
        return [n for n in num if n > 0]
class Multiply(Number,PositiveNumber):
    def __init__(self, num):
        self.num = num
    def multiplyPositive(self, num):
        positive = self.getPositive(num)
        result = 1
        if not positive:
            return 0
        for n in positive:
            result *= n
        return result
nums = eval(input("Enter a list: "))
ans = Multiply(nums)
print(ans.multiplyPositive(ans.num))