import streamlit as st
import requests

st.set_page_config(page_title="Fraud Detection", page_icon="🔍")

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
    transaction = {
        "V1": v1, "V2": v2, "V3": v3, "V4": v4, "V5": v5,
        "V6": v6, "V7": v7, "V8": v8, "V9": v9,
        "V10": 0.09, "V11": -0.55, "V12": -0.61,
        "V13": -0.99, "V14": -0.31, "V15": 1.46,
        "V16": -0.47, "V17": 0.20, "V18": 0.02,
        "V19": 0.40, "V20": 0.25, "V21": -0.01,
        "V22": 0.27, "V23": -0.11, "V24": 0.06,
        "V25": 0.12, "V26": -0.18, "V27": 0.13,
        "V28": -0.02, "Amount_scaled": amount,
        "Time_scaled": -1.99
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=transaction)
    result = response.json()

    st.markdown("---")
    if result["fraud"]:
        st.error(f"🚨 FRAUD DETECTED — Probability: {result['probability']*100:.1f}%")
    else:
        st.success(f"✅ NORMAL TRANSACTION — Fraud probability: {result['probability']*100:.1f}%")

    st.metric("Fraud Probability", f"{result['probability']*100:.1f}%")