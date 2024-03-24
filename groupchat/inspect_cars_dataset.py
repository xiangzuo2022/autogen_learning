# filename: inspect_cars_dataset.py

import pandas as pd

# Read the data from the provided file cars.csv
data = pd.read_csv('cars.csv')

# Display a sample of the dataset to inspect the column names
print(data.head())

# TERMINATE