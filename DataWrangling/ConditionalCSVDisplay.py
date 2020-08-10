# Load library
import pandas as pd
# File URL
url = './titanic.csv'
# Load data
dataframe = pd.read_csv(url)
# Show top ten rows where column 'sex' is 'male'
dataframe[dataframe['Sex'] == 'male'].head(10)