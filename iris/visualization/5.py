import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../iris.csv')

fig = plt.figure(figsize=(5, 5))
ax = fig.gca()

(iris_types, count) = np.unique(data.Species, return_counts=True)
colors = ['orange', 'blue', 'green']
i = 0
for species in iris_types:
    data[data.Species == species].plot(kind='scatter', x="PetalLengthCm",
                                       y="PetalWidthCm", color=colors[i],
                                       label=species, ax=ax)
    i = i + 1

fig.set_size_inches(12, 8)
plt.show()
