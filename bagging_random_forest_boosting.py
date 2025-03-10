# -*- coding: utf-8 -*-
"""bagging_random_forest_boosting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aFS4WqyVtleb4iRP-sqpYQn08pgjCdH7
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

filename = '/content/pima-indians-diabetes.data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = read_csv(filename, names=names)

array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
print(dataframe)

seed = 7
kfold = KFold(n_splits=10, shuffle = True, random_state=seed)
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

x=array[:,0:8]
y=array[:,8]

num_trees=100
max_features=3

kfold=KFold(n_splits=10, shuffle=True, random_state=7)
model=RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results=cross_val_score(model, x, y, cv=kfold)
print(results.mean())

#adaboost classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

filename = '/content/pima-indians-diabetes.data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = read_csv(filename, names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]

num_trees=10

seed=7

kfold=KFold(n_splits=10, shuffle=True, random_state=seed)
model=AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
results=cross_val_score(model, x, y, cv=kfold)
print(results.mean())