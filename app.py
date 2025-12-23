import streamlit as st
import joblib
import os

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)

# -----------------------------------------------------------------------------
# Custom CSS (Modern Look)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stNumberInput input {
        background-color: #262730;
        color: white;
    }
    .metric-box {
        background: linear-gradient(135deg, #1f2937, #111827);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        color: #22c55e;
        font-weight: bold;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Title Section
# -----------------------------------------------------------------------------
st.markdown("<h1 style='text-align:center;'>📊 Student Performance Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Predict performance based on study habits</p>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------------------------------------------------------
# Load Model & Scaler
# -----------------------------------------------------------------------------
MODEL_FILE = "student_performance_model.pkl"
SCALER_FILE = "scaler.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
        st.error("❌ Model or scaler file not found.")
        st.stop()

    model = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)
    return model, scaler

model, scaler = load_model()

# -----------------------------------------------------------------------------
# Input Section
# -----------------------------------------------------------------------------
st.subheader("📝 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "📘 Hours Studied (per day)",
        min_value=0.0, max_value=24.0, value=6.0, step=0.5
    )

    previous_scores = st.number_input(
        "📄 Previous Exam Score",
        min_value=0.0, max_value=100.0, value=75.0
    )

with col2:
    sample_papers = st.number_input(
        "📝 Sample Question Papers Practiced",
        min_value=0, max_value=50, value=5
    )

    sleep_hours = st.number_input(
        "😴 Sleep Hours (per day)",
        min_value=0.0, max_value=12.0, value=7.0, step=0.5
    )

st.markdown("---")

# -----------------------------------------------------------------------------
# Prediction Button
# -----------------------------------------------------------------------------
if st.button("🔮 Predict Performance", use_container_width=True):
    try:
        # IMPORTANT: Positional order MUST match training
        input_array = [[
            hours_studied,
            previous_scores,
            sample_papers,
            sleep_hours
        ]]

        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)

        st.markdown(
            f"<div class='metric-box'>🎯 Predicted Performance Index<br>{prediction[0]:.2f}</div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ using Python & Streamlit</p>",
    unsafe_allow_html=True
)
