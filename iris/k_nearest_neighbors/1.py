import pandas as pd

data = pd.read_csv("../iris.csv")
data = data.drop(columns=['Id'])

# k-nearest neighbors algorithm (k-NN) is a non-parametric method
# used for classification and regression
# The input consists of the k closest training examples in the feature space.
# In k-NN classification, the output is a class membership.
# In k-NN regression, the output is the property value for the object.

X = data.iloc[:, [0, 1, 2, 3]]
Y = data.iloc[:, 4]

print(f'attributes: {X}')
print(f'species: {Y}')
