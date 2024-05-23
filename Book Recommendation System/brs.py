import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.sparse.linalg import svds

# Sample data
data = {
    'user_id': [1, 2, 3, 4, 5],
    'book_id': [101, 102, 103, 104, 105],
    'rating': [5, 4, 3, 5, 4],
    'book_title': [
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Catcher in the Rye"
    ],
    'book_description': [
        "A novel about the American dream.",
        "A story of racial injustice in the Deep South.",
        "A dystopian novel set in a totalitarian society.",
        "A romantic novel that critiques the British landed gentry.",
        "A story about teenage angst and alienation."
    ]
}

df = pd.DataFrame(data)

# Vectorize book descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['book_description'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on content
def get_book_recommendations(title, cosine_sim=cosine_sim):
    idx = df.index[df['book_title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df['book_title'].iloc[book_indices]

# Pivot the data to create a user-book matrix
user_book_matrix = df.pivot(index='user_id', columns='book_id', values='rating').fillna(0)
user_book_matrix = user_book_matrix.values

# Perform matrix factorization
U, sigma, Vt = svds(user_book_matrix, k=2)
sigma = np.diag(sigma)

# Predict ratings
predicted_ratings = np.dot(np.dot(U, sigma), Vt)
predicted_ratings_df = pd.DataFrame(predicted_ratings, columns=df['book_id'].unique())

# Function to recommend books for a user based on collaborative filtering
def recommend_books(user_id, num_recommendations=5):
    user_row_number = user_id - 1  # User ID starts from 1
    sorted_user_ratings = predicted_ratings_df.iloc[user_row_number].sort_values(ascending=False)
    recommended_book_ids = sorted_user_ratings.head(num_recommendations).index
    recommended_books = df[df['book_id'].isin(recommended_book_ids)]['book_title']
    return recommended_books

# Command-line interface for user interaction
def main():
    print("Welcome to the Book Recommendation System!")
    user_id = int(input("Enter your user ID: "))
    print("Here are some book recommendations for you:")
    recommendations = recommend_books(user_id)
    for book in recommendations:
        print(book)

    while True:
        cont = input("Would you like to get recommendations for another book? (yes/no): ").lower()
        if cont == 'no':
            break
        book_title = input("Enter a book title you like: ")
        print("You might also like:")
        recommendations = get_book_recommendations(book_title)
        for book in recommendations:
            print(book)

if __name__ == "__main__":
    main()
