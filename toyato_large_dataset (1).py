# -*- coding: utf-8 -*-
"""toyato_large_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10pkH38z5Ps86eXQ8fmR_LPVn-I68JWhD
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.regressionplots import influence_plot
import statsmodels.formula.api as smf

from google.colab import files
uploaded=files.upload()
file_name=list(uploaded.keys())[0]

df = pd.read_excel(file_name)
df

df.shape

df.head()

# target variable price and predict the other variables

df.corr(numeric_only=True)

df.describe()

df.info()

#to check null value is there or not
df.isnull().sum()

#heat map

#remove model and fuel tank
df.drop(['Model','Fuel_Type'],axis=1,inplace=True)

#label encoder
from sklearn.preprocessing import LabelEncoder

#apply the label encoder to 7
encoder = LabelEncoder()
df["HP_encoded"] = encoder.fit_transform(df["HP"])
df["Mfg_Year_encoded"] = encoder.fit_transform(df["Mfg_Year"])
print("/nlabel encoded data")
print(df)

#apply one hot encoder
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(df[["HP", "Mfg_Month","Power_Steering"]])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(["HP","Mfg_Month","Power_Steering"]))
df = pd.concat([df, encoded_df], axis=1)
df

#prediciton