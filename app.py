
import streamlit as st
import joblib
from pathlib import Path
import numpy as np

st.set_page_config(page_title="Student Performance Predictor")

st.title("📚 Student Performance Predictor")

BASE_DIR = Path(__file__).parent

# ---- Safe model loading ----
try:
    model = joblib.load(BASE_DIR / "student_performance_model.pkl")
    scaler = joblib.load(BASE_DIR / "scaler.pkl")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

# ---- User Input ----
hours = st.number_input("Hours Studied", 0.0, 24.0, 6.0)
previous = st.number_input("Previous Score", 0.0, 100.0, 70.0)
sleep = st.number_input("Sleep Hours", 0.0, 24.0, 7.0)
papers = st.number_input("Sample Papers Practiced", 0.0, 20.0, 3.0)

if st.button("Predict Performance"):
    input_data = np.array([[hours, previous, sleep, papers]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"🎯 Predicted Performance Index: {prediction[0]:.2f}")

