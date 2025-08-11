print("By 22IT460")
menu = {
    "Paneer Butter Masala": 250,
    "Chicken Tikka": 300,
    "Paneer Tikka": 270,
    "Veg Biryani": 200,
    "Butter Naan": 50,
    "Paneer Roll": 180
}

search_word = "paneer"
search_word = search_word.lower()

for dish in menu:
    if search_word in dish.lower():
        print(dish)
