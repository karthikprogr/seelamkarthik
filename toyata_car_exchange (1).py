# -*- coding: utf-8 -*-
"""toyata_car_exchange.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_yooyl6UmcqXHYiqrHzdjKUlo_SzW8Yt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.regressionplots import influence_plot
import statsmodels.formula.api as smf
import numpy as np

import pandas as pd
from google.colab import files

# Upload dataset
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

# Load dataset
df = pd.read_csv(file_name)
df.info()

df = pd.read_csv(file_name)
df

import statsmodels.formula.api as smf

# Building an OLS model to predict price
model = smf.ols('Price ~ Age_08_04 + KM + HP + Doors + Cylinders + Gears + Weight', data=df).fit()

model.params

df.shape

model.summary()

import statsmodels.formula.api as smf
model = smf.ols('Price~KM+HP+Doors+Cylinders', data=df).fit()

# model=smf.ols('MPG~KM+HP+Doors+Cylinders',data=df).fit()

#add scatter plots for the above code
import matplotlib.pyplot as plt
plt.scatter(df['KM'],df['Price'])
plt.scatter(df['HP'],df['Price'])
plt.scatter(df['Doors'],df['Price'])
plt.scatter(df['Cylinders'],df['Price'])

sns.pairplot(df)

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Selecting numerical columns for VIF calculation
X = df[['Age_08_04', 'KM', 'HP', 'Doors', 'Cylinders', 'Gears', 'Weight']]
X['Intercept'] = 1  # Add intercept for VIF calculation

# Calculate VIF for each feature
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

vif_data  # Display the VIF data

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


# Q-Q plot for residuals
sm.qqplot(model.resid, line='q')
plt.title("Normal Q-Q plot of residuals")
plt.show()

# Residual plot
def get_standardized_values(vals):
    return (vals - vals.mean()) / vals.std()

plt.scatter(get_standardized_values(model.fittedvalues), get_standardized_values(model.resid))
plt.title('Residual Plot')
plt.xlabel('Standardized Fitted Values')
plt.ylabel('Standardized Residuals')
plt.show()

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from statsmodels.stats.outliers_influence import OLSInfluence

# Calculate Cook's Distance
influence = OLSInfluence(model)
c = influence.cooks_distance[0]  # Get Cook's distance values

# Plot Cook's Distance
plt.figure(figsize=(20, 7))
plt.stem(np.arange(len(df)), np.round(c, 3))
plt.xlabel('Row Index')
plt.ylabel("Cook's Distance")
plt.show()

# Define threshold for influential points (e.g., 4/n)
threshold = 4 / len(df)

# Identify influential points based on Cook's distance
influential_points = np.where(c > threshold)[0] #added this line to define influential_points

# Drop influential points and rebuild model
df_cleaned = df.drop(df.index[influential_points])
model_refit = smf.ols('Price ~ Age_08_04 + KM + HP + Doors + Cylinders + Gears + Weight', data=df_cleaned).fit()

model_refit.summary()

#r-squared and r-squared adjusted
#only comparing one thing
ml_W=smf.ols("Price~KM+HP",data=df).fit()
#t and pvalue
print(ml_W.tvalues,'\n',ml_W.pvalues)

#calculating VIF
rsq_hp=smf.ols("Price~KM+HP+Doors",data=df).fit().rsquared
vif_hp=1/(1-rsq_hp)

rsq_wt=smf.ols("KM~HP+Doors+Cylinders",data=df).fit().rsquared
vif_wt=1/(1-rsq_wt)

rsq_vol=smf.ols("HP~KM+Doors",data=df).fit().rsquared
vif_vol=1/(1-rsq_vol)

rsq_sp=smf.ols("Cylinders~KM+HP+Doors",data=df).fit().rsquared
vif_sp=1/(1-rsq_sp)

#storing vif values in a data frame
d1={'Variables':['KM','HP','Doors','Cylinders'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame=pd.DataFrame(d1)
Vif_frame