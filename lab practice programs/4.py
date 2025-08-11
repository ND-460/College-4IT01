print("By 22IT460")
movies = {
    "Inception": [5, 4, 5, 5, 4],
    "Interstellar": [5, 5, 4, 5],
    "The Dark Knight": [5, 5, 5, 4, 5, 5],
    "Tenet": [4, 4, 3, 4]
}
top_movie = None
highest_avg = 0
for movie, ratings in movies.items():
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating > highest_avg:
        highest_avg = avg_rating
        top_movie = movie
print("Most popular movie:", top_movie)
