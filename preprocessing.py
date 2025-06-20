import pandas as pd
import os

# Load data
ratings = pd.read_csv("data/rating_final.csv")
restaurants = pd.read_csv("data/geoplaces2.csv")
cuisines = pd.read_csv("data/chefmozcuisine.csv")

# --- Step A: Clean Ratings ---
# Drop ratings with 0
ratings = ratings[ratings['rating'] > 0]

# --- Step B: Merge restaurant info ---
# Merge ratings with restaurant info
merged = ratings.merge(restaurants, on='placeID', how='left')

# Merge cuisines into the same
merged = merged.merge(cuisines, on='placeID', how='left')

# Drop rows with missing place name or cuisine
merged = merged.dropna(subset=['name', 'Rcuisine'])

# Rename columns for clarity
merged = merged.rename(columns={
    'userID': 'User',
    'placeID': 'RestaurantID',
    'name': 'Restaurant',
    'Rcuisine': 'Cuisine',
    'rating': 'Rating'
})

# Save cleaned merged data
os.makedirs("output", exist_ok=True)
merged.to_csv("output/merged_cleaned.csv", index=False)

print("✅ Merged & cleaned data saved to 'output/merged_cleaned.csv'")
print("🔹 Sample rows:")
print(merged.head())
