# -*- coding: utf-8 -*-
"""drag_quantity_predicition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BR2FNKg2RaxQM2mjoKC9heF_C8BPJLG5
"""

import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import numpy as np

# csv_file='/content/patient_drag_quantity_data_with_30_features.csv'
df = pd.read_csv('/content/patient_drag_quantity_data_with_30_features.csv')  # Replace 'your_existing_data.csv' with the actual file path
df.to_csv(csv_file,index=False)

#load the dataset
df=pd.read_csv(csv_file)
print(df)
#preprocess categorical feature using labelEncoder
label_encoder=LabelEncoder()

#encoding categorical columns
categorical_cols=['Gender','Region','Grade Level', 'Mother Education' , 'Father Education']
for col in categorical_cols:
    df[col]=label_encoder.fit_transform(df[col])

"""head
isnull
drop
heatmap
histogram
boxplot
encoding
train_test_split
standarization
model

"""

import pickle
with open('drag_prediction.pkl','wb') as f:
  pickle.dump(model,f)
print("model has been saved a 'drag_predicition.pkl'")

from google.colab import files
files.download('drag_prediction.pkl')