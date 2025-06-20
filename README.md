🍽️ Restaurant Recommendation System

A content-based filtering system to recommend restaurants using cuisine and customer preferences. Built as a resume-level project for Data Science and AI roles.

🚀 Overview

This project is an end-to-end Restaurant Recommendation System using content-based filtering. It combines customer ratings, restaurant metadata, and cuisines to generate personalized recommendations. It includes advanced enhancements like search by cuisine, rating-based ranking, and a professional web UI using Streamlit. Built as an IIT-intern level showcase project, it emphasizes hands-on skills in data cleaning, feature engineering, and deployment.

Dataset used: Restaurant Dataset for Recommendation

📊 Key Achievements

✅ Performed advanced EDA and cleaned raw CSV data from multiple sources

✅ Merged datasets into a unified structure with customer, cuisine, and rating details

✅ Implemented content-based filtering using TF-IDF and cosine similarity

✅ Developed enhancements like search by cuisine and rating-based sorting

✅ Built an interactive Streamlit web application for real-time recommendations

✅ Packaged the entire project with clear GitHub structure and deployment-ready setup

🖠️ Features

📊 EDA and Data Cleaning: Merging, deduplication, and preprocessing

🧠 TF-IDF Based Recommendation: Uses cosine similarity on textual metadata

✅ Customer Segmentation: Rating-based filtering and insights

🔍 Search by Cuisine: Real-time filtering by preferred cuisine

⭐ Rating-Based Ranking: View top-rated restaurants per cuisine

🌐 Streamlit Interface: Smooth, clean, and responsive UI

📂 Project Structure

Restaurant_Recommendation_Project/
├── app.py                  # Streamlit frontend
├── requirements.txt        # Required libraries
├── README.md               # Project documentation
│
├── data/                   # Raw dataset CSVs
├── output/                 # Cleaned and merged data
├── notebooks/              # Python modules
│   ├── eda.py              # EDA and merging
│   ├── recommend.py        # Recommendation logic
│   └── enhancements.py     # Search & rating filters

📦 Dataset

Source: Kaggle - Restaurant Dataset for Recommendation

Files used: rating_final.csv, geoplaces2.csv, chefmozcuisine.csv

🛠️ Setup & Installation

Clone the repository:

git clone https://github.com/your-username/restaurant-recommendation-system.git
cd restaurant-recommendation-system

Create virtual environment (optional but recommended):

python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the app locally:

streamlit run app.py

Open http://localhost:8501 in your browser to use the app.

🔧 Tools & Technologies

Python: Core programming

Pandas, NumPy: Data manipulation

Scikit-Learn: TF-IDF and cosine similarity

Streamlit: Frontend interface

Jupyter Notebook: Prototyping

GitHub: Version control and hosting

👤 Contact

Sai Priya VankudothEmail: [saipriya.v.03@gmail.com]

🚀 Ready to Deploy: The app is structured and fully functional for deployment on Streamlit Cloud.

