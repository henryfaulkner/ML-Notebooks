import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../iris.csv')

species_num_series = data['Species'].value_counts()
species_num_dict = species_num_series.to_dict()

plt.figure(figsize=(5, 5))
plt.pie(species_num_dict.values(), labels=species_num_dict.keys(),
        autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.show()
