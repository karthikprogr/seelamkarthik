# -*- coding: utf-8 -*-
"""feature Engineering prima-indians-diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-FC6_rQ3bcDrVgB9I7ZE0pvE7zjfsgeD
"""

from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

filename="/content/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]

test=SelectKBest(score_func=chi2,k=4)
fit=test.fit(X,Y)
print(names)
set_printoptions(precision=3)
print(fit.scores_)
features=fit.transform(X)
# print(features[0:5,:])

"""Recursive feature elimination

"""

#RECURSIVE FEATURE ELIMINATION
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model=LogisticRegression(max_iter=400)
rfe=RFE(estimator=model,n_features_to_select=3)
fit=rfe.fit(X,Y)

fit.n_features_

fit.support_

fit.ranking_

#feature importance using decision tree
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(X,Y)
print(model.feature_importances_)





