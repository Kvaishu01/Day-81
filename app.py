import streamlit as st
import requests

st.title("🎯 Day 82 – Deploy ML Model via FastAPI + Streamlit 🚀")

st.write("Enter a value to send to the FastAPI model endpoint:")

value = st.number_input("Enter a numeric value:", step=0.1)

if st.button("Predict"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict/", json={"value": value})
        if response.status_code == 200:
            st.success(f"✅ Prediction: {response.json()['prediction']}")
        else:
            st.error("❌ API Error: Could not get prediction.")
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")

st.markdown("---")
st.markdown("🔹 Backend: FastAPI | 🔹 Frontend: Streamlit | 🔹 Model: Simple Rule-based")
