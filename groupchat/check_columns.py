# filename: check_columns.py
import pandas as pd

# Load the dataset and display the fields
data = pd.read_csv("cars.csv")
print(data.columns)