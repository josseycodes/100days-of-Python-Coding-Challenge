import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load the dataset
df = pd.read_csv('ratings.csv')

# Define the reader object
reader = Reader(rating_scale=(1, 5))

# Load the data into the surprise dataset
data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)

# Split the data into train and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train the algorithm (SVD)
algo = SVD()
algo.fit(trainset)

# Make predictions on the test set
predictions = algo.test(testset)

# Check the accuracy of the model
accuracy.rmse(predictions)

# Recommend movies for a user
def recommend_movies(user_id, num_recommendations=5):
    # List of all movie ids
    all_movie_ids = df['movieId'].unique()

    # List of movies not yet rated by the user
    movies_not_rated = []
    for movie_id in all_movie_ids:
        if not df[(df['userId'] == user_id) & (df['movieId'] == movie_id)].empty:
            continue
        movies_not_rated.append((user_id, movie_id, 4))  # Assume a default rating of 4 for unseen movies

    # Get predictions for the movies not rated by the user
    predictions = algo.test(movies_not_rated)

    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top recommendations
    top_recommendations = predictions[:num_recommendations]

    # Print recommended movies
    for i, pred in enumerate(top_recommendations, 1):
        movie_id = pred.iid
        movie_title = df[df['movieId'] == movie_id]['title'].values[0]  # Assuming the movie titles are available
        print(f"Recommendation {i}: {movie_title} (predicted rating: {pred.est})")

# Example usage
user_id = 1
recommend_movies(user_id)
