import pandas as pd

data = pd.read_csv('../iris.csv')
print(f'keys: {data.keys()}')
print(f'(len(columns), len(rows)): {data.shape}')
