print("By 22IT460")
class Palindrome:
    def __init__(self, text):
        self.text = text
    def isPalindrome(self):
        texts = self.text.replace(" ", "").lower()
        return texts == texts[::-1]
s = input("Enter a string: ")
palindrome = Palindrome(s)
print(f"Palindrome : {palindrome.isPalindrome()}")