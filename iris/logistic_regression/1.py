import pandas as pd
data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])
# Split data by species
df1 = data[data['Species'] == 'Iris-setosa']
df2 = data[data['Species'] == 'Iris-versicolor']
df3 = data[data['Species'] == 'Iris-virginica']
print('Iris-setosa')
print(df1.describe())
print('Iris-versicolor')
print(df2.describe())
print('Iris-virginica')
print(df3.describe())
