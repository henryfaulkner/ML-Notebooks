import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])
X = data.iloc[:, [0, 1, 2, 3]]
Y = data.iloc[:, 4]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3
)

print("X_train")
print(len(X_train))
print("X_test")
print(len(X_test))
