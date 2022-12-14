import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../iris.csv')

species_num_series = data['Species'].value_counts()
species_num_dict = species_num_series.to_dict()

plt.figure(figsize=(5, 5))
plt.bar(species_num_dict.keys(),
        species_num_dict.values(), color=['red', 'blue', 'green'], width=0.8)
plt.xlabel('Species')
plt.ylabel('Num Observations')
plt.title('Num Observations per Species')
plt.show()
