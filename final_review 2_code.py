# -*- coding: utf-8 -*-
"""final_review_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DsvzCBZz1_H5jdfRDpJo3pMOIyrqKbYd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from google.colab import drive
drive.mount('/content/drive')

file_path="/content/Car_Data.csv"
df=pd.read_csv(file_path)
df=pd.DataFrame(df)
df

# Initialize label encoder
le = LabelEncoder()

# Convert categorical columns to numeric
df['Company'] = le.fit_transform(df['Company'])
df['Fuel_Type'] = le.fit_transform(df['Fuel_Type'])
df['Name'] = le.fit_transform(df['Name'])
df['City'] = le.fit_transform(df['City'])

# Display the first few rows after encoding
df.head()

# Initialize StandardScaler
sc = StandardScaler()

# Scale features
scaled_features = sc.fit_transform(df)

# Convert back to DataFrame
df_scaled = pd.DataFrame(scaled_features, columns=df.columns)

# Display first few rows of scaled data
df_scaled.head()

# Compute correlation matrix
correlation_matrix = df_scaled.corr()

# Print correlation values with target variable
correlation_matrix['On_Road_Price'].sort_values(ascending=False)

# Scatter plot
plt.figure(figsize=(8,5))
plt.scatter(df['Year'], df['On_Road_Price'])
plt.scatter(df['Name'], df['On_Road_Price'])
plt.scatter(df['KM_Driven'], df['On_Road_Price'])
plt.scatter(df['Fuel_Type'], df['On_Road_Price'])
# plt.xlabel('Year')
# plt.ylabel('On Road Price')
# plt.title('Year vs On Road Price')
plt.show()

#pair plots
sns.pairplot(df)

# Compute correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation with On_Road_Price")
plt.show()

#rename
df.rename(columns={"No._of_Owners": "No_of_Owners"}, inplace=True)

# Fit the OLS model
model = smf.ols('On_Road_Price ~ Company + City + Year + KM_Driven + No_of_Owners + Fuel_Type + Calculated_Score', data=df).fit()

# Print model parameters
print(model.summary())

# Extract R-squared value
r_squared = model.rsquared
print(f"R-squared Value: {r_squared * 100:.2f}%")

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Q-Q plot for residuals
sm.qqplot(model.resid, line='q')
plt.title("Normal Q-Q plot of residuals")
plt.show()

# Residual plot
plt.figure(figsize=(8,6))
plt.scatter(model.fittedvalues, model.resid, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.grid()
plt.show()

""". Remove Multicollinearity (Check VIF)
Multicollinearity weakens the model. Let's check the Variance Inflation Factor (VIF):
"""

from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

# Drop highly correlated features
reduced_features = df[['Company', 'City', 'Year', 'No_of_Owners', 'Fuel_Type', 'Calculated_Score']]

# Compute VIF
vif_data = pd.DataFrame()
vif_data["Feature"] = reduced_features.columns
vif_data["VIF"] = [variance_inflation_factor(reduced_features.values, i) for i in range(reduced_features.shape[1])]

print("Reduced VIF Values:\n", vif_data)

""" Apply Log Transformation for Skewed Data
Non-linear relationships reduce model accuracy. Apply log transformation for KM_Driven:
"""

df['Log_KM_Driven'] = np.log1p(df['KM_Driven'])
df['Log_KM_Driven']

df['Year_City'] = df['Year'] * df['City']
df['KM_Owners'] = df['Log_KM_Driven'] * df['No_of_Owners']

df['Year_Squared'] = df['Year'] ** 2
df['KM_Driven_Squared'] = df['Log_KM_Driven'] ** 2
df['Year_Squared']
df['KM_Driven_Squared']

# Apply log transformation for highly skewed variables
df['Log_KM_Driven'] = np.log1p(df['KM_Driven'])

# Interaction terms
df['Year_City'] = df['Year'] * df['City']
df['KM_Owners'] = df['Log_KM_Driven'] * df['No_of_Owners']

# Polynomial features
df['Year_Squared'] = df['Year'] ** 2
df['KM_Driven_Squared'] = df['Log_KM_Driven'] ** 2

import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

# Define independent (X) and dependent (y) variables
X = df[['Company', 'City', 'Year', 'Log_KM_Driven', 'No_of_Owners', 'Fuel_Type', 'Calculated_Score', 'Year_City', 'KM_Owners', 'Year_Squared', 'KM_Driven_Squared']]
y = df['On_Road_Price']

# Replace infinite values with NaN
X.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill NaN values with column median
X.fillna(X.median(), inplace=True)

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add constant for the intercept term
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# Train the OLS model on training data
model = sm.OLS(y_train, X_train).fit()

# Evaluate on test data
y_pred = model.predict(X_test)

# Step 1: Identify Missing or Infinite Values
print(df.isnull().sum())  # Check NaN values
print(np.isinf(df).sum())  # Check inf values

# Step 2: Replace Inf & NaN Values
df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Convert inf to NaN
df.fillna(df.median(), inplace=True)  # Fill NaNs with median values

# Step 3: Confirm Clean Data
print(df.isnull().sum())  # Should be all zeros

from sklearn.model_selection import train_test_split

# Define independent (X) and dependent (y) variables
X = df[['Company', 'City', 'Year', 'Log_KM_Driven', 'No_of_Owners', 'Fuel_Type', 'Calculated_Score', 'Year_City', 'KM_Owners', 'Year_Squared', 'KM_Driven_Squared']]
y = df['On_Road_Price']

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df['Year_Squared'] = df['Year'] ** 2
df['Log_KM_Driven'] = np.log1p(df['KM_Driven'])

df['Year_City'] = df['Year'] * df['City']
df['KM_Owners'] = df['Log_KM_Driven'] * df['No_of_Owners']

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['Year', 'KM_Driven', 'Calculated_Score']] = scaler.fit_transform(df[['Year', 'KM_Driven', 'Calculated_Score']])

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

from sklearn.metrics import r2_score
print(f"Random Forest R² Score: {r2_score(y_test, y_pred) * 100:.2f}%")

from xgboost import XGBRegressor
xgb = XGBRegressor()
xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_test)
print(f"XGBoost R² Score: {r2_score(y_test, y_pred) * 100:.2f}%")

# Decision Tree
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print(f"Decision Tree R² Score: {r2_score(y_test, y_pred_dt) * 100:.2f}%")

# Random Forest
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print(f"Random Forest R² Score: {r2_score(y_test, y_pred_rf) * 100:.2f}%")

# Linear Regression
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print(f"Linear Regression R² Score: {r2_score(y_test, y_pred_lr) * 100:.2f}%")

# Logistic Regression (for binary classification)
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, (y_train > y_train.median()).astype(int))
y_pred_logreg = logreg.predict(X_test)

print(f"Logistic Regression Accuracy: {logreg.score(X_test, (y_test > y_test.median()).astype(int)) * 100:.2f}%")

# Multiple Regression
import statsmodels.api as sm

X_const = sm.add_constant(X_train)
multiple_regression_model = sm.OLS(y_train, X_const).fit()

print(multiple_regression_model.summary())

from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Drop the target variable
X = df.drop(columns=['On_Road_Price'])  # Features
y = df['On_Road_Price']  # Target variable

# Replace infinite values with NaN
X.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill missing values with the median of each column
X.fillna(X.median(), inplace=True)

# Encode categorical variables (if any)
label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Normalize features (Chi-square requires non-negative values)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Convert y (On_Road_Price) into categories (e.g., Low, Medium, High price)
y_binned = pd.qcut(y, q=3, labels=[0, 1, 2])  # Creates 3 categories (0=Low, 1=Medium, 2=High)

# Select top k features using chi-square test
k = 5  # Select top 5 features
selector = SelectKBest(score_func=chi2, k=k)
X_new = selector.fit_transform(X_scaled, y_binned)

# Get selected feature names
selected_features = X.columns[selector.get_support()]
print("Top", k, "Selected Features:", selected_features)

model.summary()