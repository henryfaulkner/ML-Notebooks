import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv('../iris.csv')
data = data.drop(columns=['Id'])
X = data.iloc[:, [0, 1, 2, 3]]
Y = data.iloc[:, 4]

le = LabelEncoder()
df = pd.DataFrame(Y.to_list(), columns=['species'])
Y = df[df.columns[:]].apply(le.fit_transform)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2
)

print("train")
print(X_train)
print(Y_train)
print("test")
print(X_test)
print(Y_test)
