import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API key and base URL
API_KEY = 'a3a3414b1a3d9868d9d8858d8f5cedd8'
TMDB_URL = 'https://api.themoviedb.org/3'

# Function to fetch movie poster from TMDB
def get_movie_poster(movie_title):
    try:
        search_url = f'{TMDB_URL}/search/movie?api_key={API_KEY}&query={movie_title}'
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()

        if data['results']:
            movie_id = data['results'][0]['id']
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return f'https://image.tmdb.org/t/p/w500{poster_path}'
    except Exception as e:
        print(f"Error fetching poster: {e}")
    
    return None  # Return None if poster not found or error occurs

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found."]
    
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]
    recommended_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in recommended_indices:
        title = movies.iloc[i[0]].title
        poster_url = get_movie_poster(title)
        recommendations.append((title, poster_url))
    
    return recommendations

# ---------------- Streamlit UI ----------------

st.markdown('<h1 class="title">🎬 Movie Recommender</h1>', unsafe_allow_html=True)

selected_movie = st.text_input('Search for a movie you love:')

if st.button('Recommend'):
    if selected_movie.strip() != "":
        recommendations = recommend(selected_movie)
        if recommendations[0] == "Movie not found.":
            st.error("❌ Movie not found. Please try another title.")
        else:
            st.markdown("### 🎥 Recommended Movies:")
            for title, poster in recommendations:
                if poster:
                    st.image(poster, caption=title, use_column_width=True)
                else:
                    st.write(f"• {title}")
    else:
        st.warning("⚠️ Please enter a movie title before clicking Recommend.")

# ---------------- Custom CSS Styling ----------------
st.markdown("""
    <style>
        .title {
            color: #ff6347;
            font-size: 42px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            padding-bottom: 20px;
        }
        .stButton>button {
            background-color: #ff6347;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #e5533d;
            transform: scale(1.05);
        }
        .stImage img {
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }
        body {
            background-color: #f7f7f7;
        }
    </style>
""", unsafe_allow_html=True)
