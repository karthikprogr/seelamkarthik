import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

# Title of the web app
st.title('Model Deployment: Logistic Regression')

# Sidebar for user input
st.sidebar.header('User  Input Parameters')

def user_input_features():
    # User input for various features
    CLMSEX = st.sidebar.selectbox('Gender', ('1', '0'))
    CLMINSUR = st.sidebar.selectbox('Insurance', ('1', '0'))
    SEATBELT = st.sidebar.selectbox('SeatBelt', ('1', '0'))
    CLMAGE = st.sidebar.number_input("Insert the Age", min_value=0, max_value=120, value=30)
    LOSS = st.sidebar.number_input("Insert the Loss", min_value=0.0, value=0.0)
    
    # Creating a DataFrame from user input
    data = {
        'CLMSEX': CLMSEX,
        'CLMINSUR': CLMINSUR,
        'SEATBELT': SEATBELT,
        'CLMAGE': CLMAGE,
        'LOSS': LOSS
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
df = user_input_features()

# Display user input parameters
st.subheader('User  Input parameters')
st.write(df)

# Load the dataset
claimants = pd.read_csv("claimants.csv")
claimants.drop(["CASENUM"], inplace=True, axis=1)

# Drop rows with missing values
claimants = claimants.dropna()

# Prepare features and target variable
X = claimants.iloc[:, [1, 2, 3, 4, 5]]
Y = claimants.iloc[:, 0]

# Train the Logistic Regression model
clf = LogisticRegression()
clf.fit(X, Y)

# Make predictions
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

# Display predicted result
st.subheader('Predicted Result')
st.write('Yes' if prediction[0] == 1 else 'No')

# Display prediction probabilities
st.subheader('Prediction Probabilities')
st.write(f'Probability of Yes: {prediction_proba[0][1]:.2f}')
st.write(f'Probability of No: {prediction_proba[0][0]:.2f}')