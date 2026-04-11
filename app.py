import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Fraud Detection", page_icon="🔍")

model = joblib.load("My_Fd_Model.pkl")

st.title("🔍 Real-Time Fraud Detection")
st.markdown("Enter transaction details to analyze fraud risk.")

st.subheader("📊 Transaction Data")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Amount (scaled)", value=0.24)
    v1 = st.number_input("V1", value=-1.35)
    v2 = st.number_input("V2", value=-0.07)
    v3 = st.number_input("V3", value=2.53)
    v4 = st.number_input("V4", value=1.37)

with col2:
    v5 = st.number_input("V5", value=-0.33)
    v6 = st.number_input("V6", value=0.46)
    v7 = st.number_input("V7", value=0.23)
    v8 = st.number_input("V8", value=0.09)
    v9 = st.number_input("V9", value=0.36)

if st.button("🔍 Analyze Transaction"):
    features = np.array([[
        v1, v2, v3, v4, v5, v6, v7, v8, v9,
        0.09, -0.55, -0.61, -0.99, -0.31, 1.46,
        -0.47, 0.20, 0.02, 0.40, 0.25, -0.01,
        0.27, -0.11, 0.06, 0.12, -0.18, 0.13,
        -0.02, amount, -1.99
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error(f"🚨 FRAUD DETECTED — Probability: {probability*100:.1f}%")
    else:
        st.success(f"✅ NORMAL TRANSACTION — Fraud probability: {probability*100:.1f}%")

    st.metric("Fraud Probability", f"{probability*100:.1f}%")