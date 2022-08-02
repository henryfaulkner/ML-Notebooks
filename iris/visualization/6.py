import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])

data.hist()
plt.show()
