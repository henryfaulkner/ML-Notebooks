import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])
X = data.iloc[:, [0, 1, 2, 3]]
Y = data.iloc[:, 4]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2
)

k = 5
while k != 10:
    knc = KNeighborsClassifier(n_neighbors=k)
    knc.fit(X_train, Y_train)
    print(knc.score(X_test, Y_test))
    k = k + 1
