import pandas as pd

Movie_data = {
    "Movie Title": ["M 1", "M 2", "M 3", "M 4", "M 5"],
    "Movie Revenue": [2500000, 25000000, 3000000, 500000, 54787],
    "Movie Cost": [8000000, 120000, 500000, 900000, 897778]
}

df = pd.DataFrame(Movie_data)

movies = df[(df['Movie Revenue'] > 2000000) & (df['Movie Cost'] < 1000000)]

print("Movies with Revenue > 2 million and Cost < 1 million: ")
print(movies)
