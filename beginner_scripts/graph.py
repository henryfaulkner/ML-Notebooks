# Load CSV using Pandas from URL
import pandas
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
data = data.add_prefix('test-')
#data.hist().plot(kind='box')

pandas.plotting.scatter_matrix(data)
plt.show()