import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("rf_model.pkl")

# Page title
st.title("📊 Customer Churn Prediction Dashboard")

st.write(
    "Predict whether a customer is at risk of churning based on purchasing behaviour."
)

# User inputs
frequency = st.number_input(
    "Frequency (number of purchases)",
    min_value=1,
    value=5
)

monetary = st.number_input(
    "Monetary Value (£ spent)",
    min_value=0.0,
    value=100.0
)

# Create dataframe for prediction
input_data = pd.DataFrame({
    "Frequency": [frequency],
    "Monetary": [monetary]
})

# Prediction button
if st.button("Predict Churn Risk"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.write(
        f"Churn Probability: {probability:.1%}"
    )

    if prediction == 1:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Low Churn Risk")