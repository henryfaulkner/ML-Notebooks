import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])
X = data.iloc[:, :-1]
Y = data.iloc[:, 4]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2
)

k = 5
k_list = []
train_score_list = []
test_score_list = []
while k != 10:
    knc = KNeighborsClassifier(n_neighbors=k)
    knc.fit(X_train, Y_train)
    k_list.append(k)
    train_score_list.append(knc.score(X_train, Y_train))
    test_score_list.append(knc.score(X_test, Y_test))
    k = k + 1

plt.figure(figsize=(5, 5))
plt.plot(k_list, test_score_list, label='Testing Accuracy')
plt.plot(k_list, train_score_list, label='Training Accuracy')
plt.legend()
plt.ylim([.85, 1.10])
plt.xlabel('k nearest neighbors')
plt.ylabel('accuracy score')
plt.title('Accuracy Scores per K Number Neighbors')
plt.show()
