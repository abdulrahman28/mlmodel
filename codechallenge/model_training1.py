import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datacleaning import clean as cln


def recommend_movies(user_input, movie_df, top_n=5):
    """Recommend top N movies based on text similarity."""
    # Combine user input with movie descriptions
    texts = movie_df['Description'].tolist()
    texts.insert(0, user_input)  # Insert user input at the beginning
    
    # Convert text data into TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Compute cosine similarity between user input and movie descriptions
    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]
    
    # Get top N similar movies
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    # Return recommended movies with well-formatted table
    recommended_movies = movie_df.iloc[top_indices][['Title', 'Description']]
    recommended_movies.insert(0, 'ID', range(1, len(recommended_movies) + 1))
    
    return recommended_movies

if __name__ == "__main__":
    
    # Get user input
    user_input = input(" \n Enter a short description of your preferred movie: ")
     
    fln = 'movies.csv' # Filename of the the dataset from Kaggle public repository
    
    # Load dataset
    movie_df = cln(fln) # Clean the dataset and return Title and Description
    
    # Recommend movies
    recommendations = recommend_movies(user_input, movie_df)
    
    # Display results
    print("\nTop recommended movies:")
    print(recommendations.to_string(index=False))
