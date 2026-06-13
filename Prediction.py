import streamlit as st
import pandas as pd
import joblib
import os

# Load model
model = joblib.load("models/churn_model.pkl")

st.title("🎯 Customer Churn Prediction")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

with col2:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )

if st.button("Predict Churn"):

    data = pd.DataFrame({
        "gender": [0 if gender == "Female" else 1],
        "SeniorCitizen": [senior],
        "Partner": [1 if partner == "Yes" else 0],
        "Dependents": [1 if dependents == "Yes" else 0],
        "tenure": [tenure],
        "PhoneService": [1 if phone_service == "Yes" else 0],
        "MultipleLines": [1 if multiple_lines == "Yes" else 0],
        "InternetService": [0],
        "OnlineSecurity": [0],
        "OnlineBackup": [0],
        "DeviceProtection": [0],
        "TechSupport": [0],
        "StreamingTV": [0],
        "StreamingMovies": [0],
        "Contract": [0],
        "PaperlessBilling": [0],
        "PaymentMethod": [0],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.subheader("📊 Risk Score")

    st.progress(int(probability * 100))

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

    if probability < 0.30:
        st.success("🟢 Low Risk Customer")
    elif probability < 0.70:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.error("🔴 High Risk Customer")

    if prediction == 1:
        st.error("Customer is likely to churn")
        result = "Likely to Churn"
    else:
        st.success("Customer is likely to stay")
        result = "Likely to Stay"

    # Save history
    history = pd.DataFrame({
        "Date": [pd.Timestamp.now()],
        "Prediction": [result],
        "RiskScore": [round(probability * 100, 2)]
    })

    history.to_csv(
        "prediction_history.csv",
        mode="a",
        header=False,
        index=False
    )

    st.success("Prediction saved to history")