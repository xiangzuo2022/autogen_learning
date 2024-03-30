# filename: load_data.py
import pandas as pd

data = pd.read_csv('/Users/emilyzuo/Desktop/agent/autogen_learning/groupchat/diabetes.csv')
print(data.head())