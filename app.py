import streamlit as st
import pickle
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import requests

def fetch_poster(suggestions):
    poster_urls = []
    for movie_title in suggestions:
        # Assuming your movie titles are exact matches to the movie titles in the dataset
        movie = movies[movies['Title'] == movie_title].iloc[0]
        poster_urls.append(movie['Poster_Url'])
    return poster_urls


def recommend(movie):
    emb = embed([movie])
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    recommended_movies = []
    for i in neighbors:
        recommended_movies.append(movies['Title'].iloc[i])
    poster_urls = fetch_poster(recommended_movies)
    return recommended_movies, poster_urls


movies_dict = pickle.load(open('movies_dict_u.pkl', 'rb'))
loaded_model = tf.saved_model.load("model_savedmodel")
embed = hub.KerasLayer(loaded_model)  # Use the loaded model for embedding
nn = pickle.load(open('nn.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')


selected_movie = st.selectbox(
    'Take suggestion for movies',
    ['Select or Type name of Movie'] + movies['Title'].values.tolist(), key='movie_dropdown')

if selected_movie != 'Select or Type name of Movie':
    recommendations, poster_urls = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(len(recommendations)):
        row = i // 5  # Determine the row index based on the current index
        column = i % 5  # Determine the column index based on the current index

        with locals()[f"col{column+1}"]:
            if i < len(recommendations):
                # Display movie title with spaces
                st.text(" ".join(recommendations[i].split()))
                st.image(poster_urls[i])

        if column == 4:
            # Move to the next row by creating a new set of columns
            col1, col2, col3, col4, col5 = st.columns(5)
