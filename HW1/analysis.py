import pandas as pd
from pathlib import Path

# Load the Netflix CSV file
file_path = Path(__file__).parent / "netflix_content_intelligence_combined.csv"
df = pd.read_csv(file_path)

print("TASK 1: First 2 rows")
print(df.head(2))

print("TASK 2: First row")
print(df.iloc[0])

print("TASK 3: Rows 10-19")
print(df.iloc[10:20])

print("TASK 4: Column names")
print(df.columns)

print("TASK 5: First 10 titles")
print(df["title"].head(10))

print("TASK 6: First 10 rows of title, type, and release year")
print(df[["title", "type", "release_year"]].head(10))

print("TASK 7")
# Question 1: How many Movies vs. TV Shows are in the dataset?
print("QUESTION 1: How many Movies vs. TV Shows are in the dataset?")
type_counts = df["type"].value_counts()
print(type_counts)

# Question 2: How many titles have an IMDb rating of 8.0 or higher?
print("QUESTION 2: How many titles have an IMDb rating of 8.0 or higher?")
high_rated = df[df["imdb_rating"] >= 8.0]
print(len(high_rated))

# Question 3: How many Movies have an IMDb rating of 7.0 or higher?
print("QUESTION 3: How many Movies have an IMDb rating of 7.0 or higher?")

high_rated_movies = df[
    (df["type"] == "Movie") &
    (df["imdb_rating"] >= 7.0)
]

print(len(high_rated_movies))