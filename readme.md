# Real Estate Price Prediction System (Gurugram)

This repository contains a comprehensive, end-to-end Machine Learning pipeline for predicting real estate prices in Gurugram, India. The project spans the entire data science lifecycle, from raw data cleaning and exploratory data analysis (EDA) to advanced feature engineering, predictive modeling, and building a property recommender system.

## Project Overview

The objective of this project is to accurately predict the prices of flats and houses in Gurugram based on various features such as location, property type, area, number of bedrooms, and luxury scores. 

Beyond simple price prediction, the project also extracts actionable real estate insights and features a content-based recommendation system to suggest similar properties to prospective buyers.

## Directory Structure and Workflow

The project is structured linearly across several Jupyter Notebooks, categorized by the stages of the machine learning lifecycle:

### 1. Data Collection & Preprocessing
*   **`flats.csv` & `houses.csv`**: Raw datasets scraped/collected containing property listings.
*   **`data-preprocessing-flats.ipynb` & `data-preprocessing-houses.ipynb`**: Initial cleaning of the raw data (handling messy strings, standardizing columns).
*   **`merge-flats-and-house.ipynb`**: Combines the cleaned flats and houses datasets into a single unified dataset (`gurugram_properties.csv`).
*   **`data-preprocessing-level-2.ipynb`**: Further refines the merged dataset.

### 2. Exploratory Data Analysis (EDA)
*   **`eda-univariate-analysis.ipynb`**: Analysis of individual variables to understand their distributions.
*   **`eda-multivariate-analysis.ipynb`**: Exploration of relationships between different features (e.g., price vs. area, price vs. location).
*   **`data-visualization.ipynb`**: Detailed visualizations highlighting key trends in the Gurugram real estate market.
*   **`eda-pandas-profiling.ipynb`**: Generates a comprehensive, automated HTML profiling report (`output_report.html`) summarizing data statistics.

### 3. Data Engineering & Missing Values
*   **`missing-value-imputation.ipynb`**: Strategies to handle missing data intelligently without losing valuable information.
*   **`outlier-treatment.ipynb`**: Identifies and treats statistical outliers in property prices and sizes to improve model robustness.

### 4. Feature Engineering & Selection
*   **`feature-engineering.ipynb`**: Creation of new predictive features (e.g., luxury score, age of possession) from existing data.
*   **`feature-selection.ipynb` & `feature-selection-and-feature-engineering.ipynb`**: Evaluates feature importance and drops redundant columns to prevent multicollinearity and overfitting.

### 5. Machine Learning Modeling
*   **`baseline model.ipynb`**: Establishes a simple baseline model to benchmark future complex models.
*   **`model-selection.ipynb`**: Tests and tunes various machine learning algorithms (Linear Regression, Random Forest, XGBoost, etc.) to select the best performing predictive model.

### 6. Advanced Modules
*   **`recommender-system.ipynb`**: A content-based filtering system that recommends similar properties to users based on features like location, price, and amenities.
*   **`insights-module.ipynb`**: Analyzes the model and dataset to extract business insights regarding the real estate market in Gurugram.

## Key Files
*   **`output_report.html`**: The automated data profiling report.
*   **`gurugram_properties_post_feature_selection_v2.csv`**: The final dataset used for training the machine learning models.
*   **`latlong.csv`**: Latitude and longitude coordinates used for geospatial analysis of properties.

## Getting Started

1. Clone the repository.
2. Install the necessary Python packages (Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, XGBoost).
3. Follow the notebooks in chronological order (Preprocessing -> EDA -> Feature Engineering -> Modeling) to reproduce the pipeline.