import streamlit as st
import pandas as pd

st.title("📜 Prediction History")

try:
    history = pd.read_csv("prediction_history.csv")

    total_predictions = len(history)

    st.subheader(f"Total Predictions: {total_predictions}")

    st.dataframe(history, use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}")