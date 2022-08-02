import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("../iris.csv")
data.describe().plot(kind='area', fontsize=16, figsize=(
    15, 8), table=False, colormap='Accent')
plt.xlabel('Stats')
plt.ylabel('Value')
plt.title('General Stats of the Iris Dataset')
plt.show()
