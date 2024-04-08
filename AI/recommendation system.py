import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie ratings data (user-item matrix)
ratings_data = {
    'User1': {'Interstellar': 5, 'Inception': 4, 'The Dark Knight': 4, 'The Matrix': 3, 'Avatar': 2},
    'User2': {'Interstellar': 5, 'Inception': 5, 'The Dark Knight': 4, 'The Matrix': 3, 'Avatar': 2},
    'User3': {'Interstellar': 4, 'Inception': 4, 'The Dark Knight': 5, 'The Matrix': 3, 'Avatar': 3},
    'User4': {'Interstellar': 3, 'Inception': 3, 'The Dark Knight': 4, 'The Matrix': 5, 'Avatar': 4},
    'User5': {'Interstellar': 2, 'Inception': 3, 'The Dark Knight': 4, 'The Matrix': 5, 'Avatar': 5}
}

# Create a DataFrame from the ratings data
ratings_df = pd.DataFrame(ratings_data)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(ratings_df.T)

# Function to recommend movies for a given user
def recommend_movies(user, n=3):
    user_index = ratings_df.columns.get_loc(user)
    similar_users = user_similarity[user_index]
    similar_users_indices = similar_users.argsort()[::-1][1:]  # Exclude the user itself
    recommended_movies = set()
    for index in similar_users_indices:
        similar_user = ratings_df.columns[index]
        for movie, rating in ratings_data[similar_user].items():
            if ratings_data[user].get(movie) is None:
                recommended_movies.add(movie)
    return list(recommended_movies)[:n]

# Example usage
user = 'User1'
recommended_movies = recommend_movies(user, n=3)
print(f"Recommended movies for {user}: {recommended_movies}")
