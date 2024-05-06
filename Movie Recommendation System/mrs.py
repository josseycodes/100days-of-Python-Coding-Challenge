import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import cross_validate

# Load the MovieLens dataset
ratings = pd.read_csv('ratings.csv')

# Define the rating scale
reader = Reader(rating_scale=(1, 5))

# Load the dataset into Surprise's data format
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Use user-based collaborative filtering with cosine similarity
sim_options = {
    'name': 'cosine',
    'user_based': True
}

# Initialize the KNNBasic model
knn_model = KNNBasic(sim_options=sim_options)

# Train the model
trainset = data.build_full_trainset()
knn_model.fit(trainset)

# Make predictions for all pairs (user, item) that are not in the training set
testset = trainset.build_anti_testset()
predictions = knn_model.test(testset)

# Function to get top N movie recommendations for a given user
def get_top_n_recommendations(predictions, userId, n=10):
    # Filter predictions for the given user
    user_predictions = [pred for pred in predictions if pred.uid == userId]
    # Sort predictions by estimated rating
    user_predictions.sort(key=lambda x: x.est, reverse=True)
    # Get top N recommendations
    top_n = user_predictions[:n]
    return [(pred.iid, pred.est) for pred in top_n]

# Example usage: Get top 10 recommendations for user 1
user_id = 1
top_recommendations = get_top_n_recommendations(predictions, user_id)
print("Top 10 movie recommendations for User", user_id, ":")
for movie_id, est_rating in top_recommendations:
    print("Movie ID:", movie_id, "| Estimated Rating:", est_rating)
