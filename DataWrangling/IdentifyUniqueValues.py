# Load library
import pandas as pd
# Create URL
url = 'titanic.csv'
# Load data
dataframe = pd.read_csv(url)
# Select unique values
dataframe['Sex'].unique()
#array(['female', 'male'], dtype=object)