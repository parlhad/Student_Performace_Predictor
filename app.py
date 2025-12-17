import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# -----------------------------------------------------------------------------
# 1. App Configuration
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Student Performance Prediction", layout="centered")

st.title("📚 Student Performance Predictor")
st.write("Enter the student's details below to predict their performance.")

# -----------------------------------------------------------------------------
# 2. Load the Model and Scaler
# -----------------------------------------------------------------------------
# Using the exact filenames you provided
MODEL_FILE = 'student_performance_model.pkl'
SCALER_FILE = 'scaler.pkl'

@st.cache_resource
def load_modules():
    # Load the Model
    if not os.path.exists(MODEL_FILE):
        st.error(f"File not found: {MODEL_FILE}")
        st.stop()
    
    # Load the Scaler (Preprocessor)
    if not os.path.exists(SCALER_FILE):
        st.error(f"File not found: {SCALER_FILE}")
        st.stop()

    with open(MODEL_FILE, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    with open(SCALER_FILE, 'rb') as scaler_file:
        loaded_scaler = pickle.load(scaler_file)
        
    return loaded_model, loaded_scaler

try:
    model, scaler = load_modules()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. Input Form
# -----------------------------------------------------------------------------
with st.form("student_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["female", "male"])
        race_ethnicity = st.selectbox("Race/Ethnicity", [
            "group A", "group B", "group C", "group D", "group E"
        ])
        parental_level_of_education = st.selectbox("Parental Education", [
            "some high school", "high school", "some college", 
            "associate's degree", "bachelor's degree", "master's degree"
        ])

    with col2:
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        test_preparation_course = st.selectbox("Test Prep Course", [
            "none", "completed"
        ])
        
    st.markdown("---")
    st.subheader("Current Scores")
    
    c1, c2 = st.columns(2)
    with c1:
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
    with c2:
        writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

    # Submit Button
    submitted = st.form_submit_button("Predict Result")

# -----------------------------------------------------------------------------
# 4. Prediction Logic
# -----------------------------------------------------------------------------
if submitted:
    # Prepare the input data matches the columns used in 'First.ipynb'
    input_df = pd.DataFrame({
        'gender': [gender],
        'race_ethnicity': [race_ethnicity],
        'parental_level_of_education': [parental_level_of_education],
        'lunch': [lunch],
        'test_preparation_course': [test_preparation_course],
        'reading_score': [reading_score],
        'writing_score': [writing_score]
    })

    try:
        # Step 1: Transform data using the scaler
        # (Assuming 'scaler.pkl' handles OneHotEncoding + Scaling)
        final_input = scaler.transform(input_df)
        
        # Step 2: Predict
        prediction = model.predict(final_input)
        
        # Step 3: Display
        st.success(f"🎯 Predicted Math Score: **{prediction[0]:.2f}**")
        
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.info("Note: Ensure your 'scaler.pkl' is a Pipeline/ColumnTransformer that handles categorical data.")