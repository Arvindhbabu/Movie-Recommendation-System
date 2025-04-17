# 🎬 Movie Recommendation System

This is a content-based Movie Recommendation System built with **Python**, **Streamlit**, and **scikit-learn**. It suggests movies similar to the one you like based on their content (like genres, cast, keywords, etc.).

Live Demo: [movie-recommendation-system.streamlit.app](https://movie-recommendation-system.streamlit.app) *(replace this with your actual deployed URL)*

## 🔍 Features

- Recommend similar movies based on a selected movie
- View movie posters fetched from **TMDB API**
- Fast and interactive **Streamlit UI**
- Lightweight and beginner-friendly ML project

---

## 🚀 How It Works

- Preprocessed movie metadata is vectorized using **TF-IDF** / **CountVectorizer**
- A **cosine similarity matrix** is built between all movies
- Based on the selected movie, the system fetches the top N most similar ones

---

## 🧠 Tech Stack

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Pickle (for model serialization)
- TMDB API (for fetching posters)

---

## 📁 Project Structure

```bash
Movie-Recommendation-System/
├── app.py                     # Main Streamlit app
├── movies.pkl                 # Pickled movie data
├── similarity.pkl             # Pickled similarity matrix
├── requirements.txt           # Dependencies
└── README.md                  # You're here
