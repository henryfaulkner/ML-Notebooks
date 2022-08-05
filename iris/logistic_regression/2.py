import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../iris.csv')

fig = data[data.Species == 'Iris-setosa'].plot(
    kind='scatter', x='SepalLengthCm', y='PetalWidthCm', color='orange', label='Setosa')
data[data.Species == 'Iris-versicolor'].plot(
    kind='scatter', x='SepalLengthCm', y='PetalWidthCm', color='blue', label='versicolor', ax=fig)
data[data.Species == 'Iris-virginica'].plot(
    kind='scatter', x='SepalLengthCm', y='PetalWidthCm', color='green', label='virginica', ax=fig)

print(type(fig))
fig.set_xlabel("Sepal Length")
fig.set_ylabel("Petal Width")
fig.set_title("Sepal Length VS Petal Width")
fig = plt.gcf()
fig.set_size_inches(12, 8)
plt.show()
