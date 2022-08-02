import pandas as pd

data = pd.read_csv('../iris.csv')
print(f'data stats: {data.describe()}')
