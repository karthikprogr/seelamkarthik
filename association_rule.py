# -*- coding: utf-8 -*-
"""Association rule.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/133ovGOL_Gwm3a9brtYhUD1GfKXzTS24K
"""

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

from google.colab import drive
drive.mount('/content/drive')

file_name="/content/Titanic.csv"

titanic=pd.read_csv(file_name)
titanic

#encoding
titanic.isnull().sum()

#preprocessing
df=pd.get_dummies(titanic)
df.head()

#apriori algorithm
frequent_itemset=apriori(df,min_support=0.1,use_colnames=True)
frequent_itemset

rules=association_rules(frequent_itemset, metric="lift",min_threshold=0.7)
rules

rules.sort_values('lift',ascending=False)[0:20]

rules[rules.lift>1]



