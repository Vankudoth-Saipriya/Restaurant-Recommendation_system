# notebooks/eda.py

import pandas as pd
import os

# Load all relevant datasets
ratings = pd.read_csv("data/rating_final.csv")
restaurants = pd.read_csv("data/geoplaces2.csv")
cuisines = pd.read_csv("data/chefmozcuisine.csv")

# Merge ratings with restaurants to get names
merged = ratings.merge(restaurants, on='placeID', how='left')

# Merge again to get cuisine information
merged = merged.merge(cuisines, on='placeID', how='left')

# Drop rows with missing restaurant name or cuisine
merged = merged.dropna(subset=['name', 'Rcuisine'])

# Select relevant columns
merged = merged[['userID', 'placeID', 'name', 'Rcuisine', 'rating']]

# Optional: Rename for clarity
merged.rename(columns={
    'userID': 'User',
    'placeID': 'Place',
    'name': 'Restaurant',
    'Rcuisine': 'Cuisine',
    'rating': 'Rating'
}, inplace=True)

# Save cleaned output
os.makedirs("output", exist_ok=True)
merged.to_csv("output/merged_cleaned.csv", index=False)

print("✅ Cleaned and merged data saved to 'output/merged_cleaned.csv'")
