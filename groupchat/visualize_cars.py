# filename: visualize_cars.py
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from cars.csv
data = pd.read_csv('work_dir/cars.csv')

# Print the fields in the dataset
print(data.columns)

# Plot a visualization of the relationship between weight and horsepower
plt.figure(figsize=(10, 6))
plt.scatter(data['Weight'], data['Horsepower'], color='b', alpha=0.5)
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('work_dir/weight_vs_horsepower_plot.png')

plt.show()