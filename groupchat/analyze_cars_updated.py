# filename: analyze_cars_updated.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the provided file cars.csv
data = pd.read_csv('cars.csv')

# Perform data cleaning and transformation if necessary (e.g., handling missing values or outliers)

# Plot a visualization showing the relationship between weight and horsepower with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Weight', y='Horsepower', data=data, scatter_kws={'alpha':0.5})
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('weight_vs_horsepower_updated.png')

plt.show()  # Display the plot

# TERMINATE