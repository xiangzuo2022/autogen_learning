# filename: load_diabetes_data.py
import pandas as pd

# Load the data
data = pd.read_csv('./groupchat/diabetes.csv')

# Display the first few rows of the data to understand its structure
print(data.head())