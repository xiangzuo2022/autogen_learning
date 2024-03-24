# filename: visualize_cars_relationship.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the provided file cars.csv
data = pd.read_csv('cars.csv')

# Update the column names for 'Weight' and 'Horsepower' based on the dataset inspection
weight_column = 'Width'  # Update with the correct column name for weight
horsepower_column = 'Len'  # Update with the correct column name for horsepower

# Plot a visualization showing the relationship between weight and horsepower with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x=weight_column, y=horsepower_column, data=data, scatter_kws={'alpha': 0.5})
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('weight_vs_horsepower_visualization.png')

plt.show()  # Display the plot

# TERMINATE