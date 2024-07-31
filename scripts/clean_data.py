# Data Preprocessing and Cleaning 

import pandas as pd

# Load the downloaded data
data = pd.read_csv('data/GSE12345_samples.csv', index_col=0)

# Display the first few rows of the data
print("Original Data:")
print(data.head())

# Remove duplicates
data = data.drop_duplicates()

# Handle missing values (e.g., fill with mean of the column)
data = data.fillna(data.mean())

# Normalize the data (z-score normalization)
data = (data - data.mean()) / data.std()

# Save the cleaned data
data.to_csv('data/GSE12345_samples_cleaned.csv')

# Display the first few rows of the cleaned data
print("Cleaned Data:")
print(data.head())

