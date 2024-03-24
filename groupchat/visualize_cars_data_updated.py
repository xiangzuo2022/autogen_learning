# filename: visualize_cars_data_updated.py
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Download the dataset
url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
response = requests.get(url)
with open("cars.csv", "wb") as file:
    file.write(response.content)

# Load the dataset
data = pd.read_csv("cars.csv")

# Plot the relationship between weight and horsepower
plt.figure(figsize=(10, 6))
plt.scatter(data['Weight'], data['Horsepower(HP)'], color='b', alpha=0.5)
plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.savefig('weight_vs_horsepower.png')

plt.show()