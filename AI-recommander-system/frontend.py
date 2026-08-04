import streamlit as st
import pickle

movies_df = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = movies_df['title'].values

st.title("Movie Recommender System")

selected_movies = st.selectbox('Select Movie:', movies)


def recommended(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies


if st.button('Recommend'):
    recommendations = recommended(selected_movies)
    for i in recommendations:
        st.write(i)
