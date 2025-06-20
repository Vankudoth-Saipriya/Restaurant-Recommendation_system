# notebooks/recommend.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the cleaned merged data
df = pd.read_csv("output/merged_cleaned.csv")

# Combine restaurant and cuisine for vectorization
df['combined'] = df['Restaurant'].astype(str) + " " + df['Cuisine'].astype(str)

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Cosine similarity calculation
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Mapping from restaurant name to index
indices = pd.Series(df.index, index=df['Restaurant']).drop_duplicates()

# Recommendation function
def recommend(restaurant_name, num_recommendations=5):
    matched_indices = df[df['Restaurant'] == restaurant_name].index.tolist()
    
    if not matched_indices:
        print(f"❌ '{restaurant_name}' not found in the database.\n")
        print("🔍 Example restaurant names you can try:")
        print(df['Restaurant'].dropna().unique()[:10])
        return

    # Just pick the first matched restaurant index
    idx = matched_indices[0]

    # Compute cosine similarities
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclude itself and get top recommendations
    sim_scores = [score for score in sim_scores if score[0] != idx][:num_recommendations]
    restaurant_indices = [i[0] for i in sim_scores]

    print(f"\n✅ Recommendations similar to '{restaurant_name}':\n")
    print(df[['Restaurant', 'Cuisine']].iloc[restaurant_indices].drop_duplicates().reset_index(drop=True))

# Try one:")

recommend("Luna Cafe")