# filename: analyze_cars_updated_v2.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the provided file cars.csv
data = pd.read_csv('cars.csv')

# Check the column names in the dataset
print(data.columns)

# Update the column names if they are different
# Replace 'Horsepower' and 'Weight' with the actual column names from the dataset
# For example, if the column names are 'horsepower' and 'weight', update them accordingly

# Plot a visualization showing the relationship between weight and horsepower with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='weight', y='horsepower', data=data, scatter_kws={'alpha':0.5})
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('weight_vs_horsepower_updated_v2.png')

plt.show()  # Display the plot

# TERMINATE