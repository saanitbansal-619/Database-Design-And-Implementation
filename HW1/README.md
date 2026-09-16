# Netflix Content Data Analysis

## Why I Chose This Dataset
I chose this Netflix dataset because it contains information about a large collection of movies and TV shows. It includes useful categories such as content type, release year, IMDb rating, genre, and country. This gives me different ways to filter, count, and compare the data.

## Data Questions
### Question 1: How many Movies vs. TV Shows are in the dataset?
Output:
- Movies: 5,376
- TV Shows: 2,410
The dataset has a "type" column that identifies each title as either a Movie or TV Show. Because every row represents a title, I can group and count the values in this column to answer the question.

### Question 2: How many titles have an IMDb rating of 8.0 or higher?
Output:
- 372 titles
The dataset contains an "imdb_rating" column with numerical ratings for titles. This allows me to filter the rows where the IMDb rating is greater than or equal to 8.0 and count the results.

### Question 3: How many Movies have an IMDb rating of 7.0 or higher?
Output:
- 1,097 Movies
The dataset contains both a "type" column and an "imdb_rating" column.
This allows me to use two conditions at the same time: the content must be a Movie and its IMDb rating must be 7.0 or higher.


## What the Data Cannot Answer
One question I cannot answer from this dataset is why viewers liked or disliked a particular movie or TV show. The dataset provides ratings and information about the content, but it does not contain individual viewer reviews or explanations for their ratings. What if I like jumpscares but not everyone else liking or disliking horror movies does? Assuming that a high rating means everyone enjoyed the content would be misleading because people can have different opinions and reasons for giving a rating.