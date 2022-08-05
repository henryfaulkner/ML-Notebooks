import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('../iris.csv')
data.drop(columns=['Id'])

X = data.iloc[:, :-1]
Y = data.iloc[:, 4]

le = preprocessing.LabelEncoder()
Y = le.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3
)

lr = LogisticRegression(random_state=0, solver='lbfgs',
                        multi_class='multinomial')
lr.fit(X_train, Y_train)
print('Prediction:')
prediction = lr.predict(X_test)
print(prediction)
print('Acceracy:')
print(lr.score(X_test, Y_test))
print(metrics.accuracy_score(prediction, Y_test))
