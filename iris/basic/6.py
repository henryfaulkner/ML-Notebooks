import pandas as pd

data = pd.read_csv('../iris.csv')
observations = data['Species'].value_counts()
print(f'species observations: {observations}')
