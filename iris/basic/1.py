import pandas as pd

data = pd.read_csv('../iris.csv')
print(f'shape: {data.shape}')
print(f'data type: {data.dtypes}')
print(f'first 3 rows: {data.head(3)}')
