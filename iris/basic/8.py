import pandas as pd
import numpy as np

data = pd.read_csv('../iris.csv')
print("Original Data:")
print(data.head())
data = data.drop('Id', axis=1)
print("After removing id column:")
print(data.head())
x = data.iloc[np.arange(0, 5, 1, dtype=int), [0, 1, 2, 3]].values
print(x)
