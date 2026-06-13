import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Customer Churn Prediction System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("📊 AI Customer Churn Prediction System")
st.markdown(
    """
    Predict customer churn using Machine Learning and gain business insights
    through analytics and prediction history.
    """
)

# Metrics Section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "Random Forest")

with col2:
    st.metric("Project Type", "Classification")

with col3:
    st.metric("Dataset", "Telco Churn")

st.divider()

# Features Section
st.subheader("🚀 Project Features")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    🤖 Customer Churn Prediction
    
    Predict whether a customer is likely to leave the company.
    """)

    st.info("""
    📜 Prediction History
    
    Track and review previous predictions.
    """)

with col2:
    st.info("""
    📊 Analytics Dashboard
    
    Visualize churn trends and customer behavior.
    """)

    st.info("""
    📈 Risk Assessment
    
    Calculate churn probability and risk level.
    """)

st.divider()

# Workflow Section
st.subheader("🔄 Workflow")

st.markdown("""
1. Navigate to **Prediction** page.
2. Enter customer information.
3. Generate churn prediction.
4. View churn probability score.
5. Analyze results in Analytics page.
6. Review past predictions in History page.
""")

st.divider()

# Technology Stack
st.subheader("🛠️ Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Plotly
- Joblib
""")

st.divider()

# Footer
st.success(
    "Use the sidebar on the left to access Prediction, Analytics and History pages."
)