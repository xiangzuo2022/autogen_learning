# filename: analyze_cars_updated_v3.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the provided file cars.csv
data = pd.read_csv('cars.csv')

# Display the column names in the dataset
print(data.columns)

# Update the column names based on the actual column names in the dataset
# Replace 'Horsepower' and 'Weight' with the correct column names

# Plot a visualization showing the relationship between weight and horsepower with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='actual_weight_column_name', y='actual_horsepower_column_name', data=data, scatter_kws={'alpha':0.5})
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('weight_vs_horsepower_updated_v3.png')

plt.show()  # Display the plot

# TERMINATE