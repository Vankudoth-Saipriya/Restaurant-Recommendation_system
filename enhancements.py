# notebooks/enhancements.py

import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("output/merged_cleaned.csv")

# Rename columns
df = df.rename(columns={
    'User': 'userID',
    'Place': 'placeID',
    'Restaurant': 'name',
    'Cuisine': 'Rcuisine',
    'Rating': 'rating'
})

# Function: Search top restaurants by cuisine
def search_by_cuisine(cuisine_input):
    matching = df[df['Rcuisine'].str.lower().str.contains(cuisine_input.lower())]
    
    if matching.empty:
        print(f"❌ No restaurants found for cuisine: {cuisine_input}")
        return
    
    result = (
        matching.groupby(['name', 'Rcuisine'])['rating']
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    print(f"\n🍽 Top restaurants for cuisine: {cuisine_input.lower()}")
    print(result)

# Function: Filter restaurants by minimum average rating
def filter_by_rating(min_rating):
    filtered = (
        df.groupby(['name', 'Rcuisine'])['rating']
        .mean()
        .reset_index()
    )
    filtered = filtered[filtered['rating'] >= min_rating]

    if filtered.empty:
        print(f"❌ No restaurants with rating ≥ {min_rating}")
    else:
        print(f"\n🌟 Restaurants with rating ≥ {min_rating}")
        print(filtered.sort_values(by='rating', ascending=False).head(10))

# ✅ New Function: Rank restaurants by popularity
def rank_by_popularity():
    popularity = (
        df.groupby(['name', 'Rcuisine'])
        .agg(num_ratings=('rating', 'count'), avg_rating=('rating', 'mean'))
        .reset_index()
    )

    popular_sorted = popularity.sort_values(by='num_ratings', ascending=False).head(10)

    print("\n🔥 Top 10 Most Popular Restaurants (by number of ratings):")
    print(popular_sorted)

# ================== Interactive Menu ==================
while True:
    print("\n🔘 Choose an option:")
    print("1. Search top restaurants by cuisine")
    print("2. Filter restaurants by minimum rating")
    print("3. Rank top restaurants by popularity")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        cuisine = input("🔍 Enter a cuisine to search: ")
        search_by_cuisine(cuisine)
    elif choice == "2":
        try:
            min_rating = float(input("⭐ Enter minimum average rating (0–2.5): "))
            filter_by_rating(min_rating)
        except ValueError:
            print("⚠️ Please enter a valid number (e.g., 1.5)")
    elif choice == "3":
        rank_by_popularity()
    elif choice == "4":
        print("👋 Exiting. Done!")
        break
    else:
        print("❗ Invalid choice. Try again.")
