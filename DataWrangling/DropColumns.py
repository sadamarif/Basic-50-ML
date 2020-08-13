# Load library
import pandas as pd
# File URL
url = 'titanic.csv'
# Load data
dataframe = pd.read_csv(url)
# Delete column and display 10 rows
dataframe.drop('Sex', axis=1).head(10)

# Drop multiple columns and display 10 rows
dataframe.drop(['Sex', 'Survived'], axis=1).head(10)