print("By 22IT460")
library_books = {
    "To Kill a Mockingbird": 3,
    "1984": 1,
    "The Great Gatsby": 0,
    "Pride and Prejudice": 5,
    "Moby Dick": 1,
    "The Catcher in the Rye": 2
}
print("Books with less than 2 copies available:")
for title in library_books:
    if library_books[title] < 2:
        print(title)