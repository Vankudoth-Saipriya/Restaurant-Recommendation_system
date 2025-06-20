import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load merged data
df = pd.read_csv("merged_cleaned.csv")

# Add combined feature for similarity
df['combined'] = df['Restaurant'].astype(str) + " " + df['Cuisine'].astype(str)

# Compute similarity matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix)

# Title
st.title("🍽️ Restaurant Recommendation System")

# --- Tab 1: Recommend Similar Restaurants
st.header("🔍 Get Similar Restaurant Recommendations")

restaurant_name = st.selectbox("Choose a restaurant", df['Restaurant'].unique())

def recommend(restaurant_name, num=5):
    idx = df[df['Restaurant'] == restaurant_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    restaurant_indices = [i[0] for i in sim_scores]
    return df[['Restaurant', 'Cuisine', 'Rating']].iloc[restaurant_indices]

if st.button("Recommend"):
    recommendations = recommend(restaurant_name)
    st.write("✅ Top Recommendations:")
    st.dataframe(recommendations)
    recommendations.to_csv("streamlit_recommendations.csv", index=False)
    st.success("Saved as 'streamlit_recommendations.csv'")

# --- Tab 2: Search by Cuisine
st.header("🍜 Search Top Restaurants by Cuisine")

cuisine_input = st.text_input("Enter a cuisine (e.g., Chinese, Mexican)")
min_rating = st.slider("Minimum Average Rating", 0.0, 2.0, 1.0, step=0.1)

if st.button("Search Cuisine"):
    df['Cuisine_lower'] = df['Cuisine'].str.lower()
    matching = df[df['Cuisine_lower'].str.contains(cuisine_input.lower())]
    top_cuisine = matching.groupby(['Restaurant', 'Cuisine'])['Rating'].mean()
    top_cuisine = top_cuisine[top_cuisine >= min_rating].sort_values(ascending=False).reset_index()
    st.write(f"🍴 Top {cuisine_input.title()} Restaurants with {min_rating}+ Rating:")
    st.dataframe(top_cuisine)
    top_cuisine.to_csv("cuisine_search.csv", index=False)
    st.success("Saved as 'cuisine_search.csv'")

# --- Tab 3: Top-N Most Popular
st.header("🔥 Most Popular Restaurants (by # of Ratings)")

top_n = st.slider("Select Top-N Restaurants", 5, 50, 10)

if st.button("Show Popular"):
    popular = df.groupby(['Restaurant', 'Cuisine'])['Rating'].count().sort_values(ascending=False).head(top_n).reset_index()
    popular.columns = ['Restaurant', 'Cuisine', 'Rating Count']
    st.dataframe(popular)
    popular.to_csv("popular_restaurants.csv", index=False)
    st.success("Saved as 'popular_restaurants.csv'")
