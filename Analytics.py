import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Churn Analytics")

df = pd.read_csv("data/customer_churn.csv")

fig1 = px.histogram(
    df,
    x="gender",
    color="Churn",
    title="Churn by Gender"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    title="Churn by Contract Type"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(
    df,
    x="InternetService",
    color="Churn",
    title="Churn by Internet Service"
)

st.plotly_chart(fig3, use_container_width=True)