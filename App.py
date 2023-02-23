import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    poster_path=data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "data:image/jpeg;base64,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"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies=pickle.load(open('movies.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'Search and select the name of the movie:',
    (movies['title'].values)
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.markdown(names[0])
        st.image(posters[0])
    with col2:
        st.markdown(names[1])
        st.image(posters[1])
    with col3:
        st.markdown(names[2])
        st.image(posters[2])
    with col4:
        st.markdown(names[3])
        st.image(posters[3])
    with col5:
        st.markdown(names[4])
        st.image(posters[4])
