# -*- coding: utf-8 -*-
"""news_paper_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZAHL0VFz2vfuG6E5WSx9fpRIVWx5gbdS
"""

import pandas as pd
from google.colab import files

# Step 1: Upload the CSV file
uploaded = files.upload()  # This will prompt you to upload a file

# Step 2: Get the uploaded file name
file_name = list(uploaded.keys())[0]  # Automatically retrieves the uploaded file name

# Step 3: Read the uploaded CSV file into a DataFrame
df = pd.read_csv(file_name)

# Display the first few rows of the DataFrame
df.head()

df.shape

df.corr(numeric_only=True)

import seaborn as sns
sns.distplot(df['daily'])

sns.distplot(df['sunday'])

