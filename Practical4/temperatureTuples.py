print("By 22IT460")
value = float(input("Enter temperature: "))
unit = input("Enter unit: ")
temp = (value,unit)
val,unit = temp
if unit == "C":
    converted = value * 1.8 + 32
    res = (converted,'F')
elif unit == "F":
    converted = (value - 32) * (5/9)
    res = (converted,'C')
else:
    res = ("Invalid unit",None)
print("Converted Temperature: ",res)