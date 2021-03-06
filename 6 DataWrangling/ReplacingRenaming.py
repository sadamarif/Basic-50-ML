
# Load library
import pandas as pd
# File URL
url = 'titanic.csv'
# Load data
dataframe = pd.read_csv(url)
# Replace female with Women and male with men
dataframe['Sex'].replace(["female", "male"], ["Women", "Men"]).head(10)

# Rename multiple columns
dataframe.rename(columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(10)