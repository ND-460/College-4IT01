print("By 22IT460")
cart = [
    ("T-shirt", 2, 499),
    ("Jeans", 1, 1299),
    ("Shoes", 1, 2499),
    ("Cap", 3, 299)
]
total_amount = 0
for item in cart:
    total_amount += item[1] * item[2]
print("Total payable amount:", total_amount)