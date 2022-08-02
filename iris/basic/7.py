import pandas as pd

data = pd.read_csv('../iris.csv')
print(f'data: {data}')
data = data.drop(columns=['Id'])
print(f'modified data: {data}')
