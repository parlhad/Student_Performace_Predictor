# 📊 Student Performance Predictor

## 🎯 Overview

**Student Performance Predictor** is a modern Machine Learning web application built using **Python**, **scikit-learn**, and **Streamlit**.  
It predicts a student’s performance score based on study habits and behavioral inputs such as study hours, previous scores, number of practiced question papers, and daily sleep hours.

This project demonstrates the **complete lifecycle of an ML solution** —  
from data preprocessing, model training, and serialization, to clean deployment in a real-world web interface — making it ideal for showcasing skills to **recruiters, interviewers, and project reviewers**.

---

## 🚀 Live Demo (Interactive Web App)

🔗 **Live Application:**  
👉 https://studentperformacepredictor-ychwi4g75w8xvkqqvdux4i.streamlit.app/

Use the live app to:
- Enter student study details
- Get instant performance predictions
- Experience a real deployed ML model

---

## 🔍 Key Features

✔ Predicts student performance using machine learning regression  
✔ Integrated data preprocessing and feature scaling  
✔ Clean, modern, and responsive UI built with Streamlit  
✔ End-to-end ML pipeline (training → serialization → deployment)  
✔ Real-time predictions with interactive inputs  
✔ Dataset-consistent feature handling  
✔ Resume-ready, interview-ready, and production-style project  

---

## 🎓 Problem Statement

Predicting how students will perform based on daily routines and study habits is valuable for **educators, institutions, and students**.

This project enables:
- Performance forecasting
- Study habit analysis
- Data-driven academic insights

It demonstrates how machine learning can be applied to **real-world educational scenarios**.

---

## 📦 Repository Structure
# Student Performance Predictor 🎓

A machine learning-powered web application that predicts a student's final grade based on various academic and demographic features. This project uses a Regression model to provide real-time predictions via a user-friendly Streamlit interface.

## 📌 Project Overview
The goal of this project is to analyze the factors that influence student performance and provide a tool for educators and students to estimate future outcomes. 

### Features:
* **Predictive Modeling:** Uses a trained Machine Learning model (`.pkl`) to estimate scores.
* **Interactive UI:** Built with Streamlit for a seamless user experience.
* **Data Preprocessing:** Includes a standardized scaler to ensure input consistency.
* **Reproducible:** Full training logic is documented in the Jupyter Notebook.

## 📂 Project Structure
```text
Student_Performace_Predictor/
├── app.py                        # Streamlit web application
├── First.ipynb                   # Model training & experimentation notebook
├── student_performance_model.pkl # Trained ML regression model
├── scaler.pkl                    # Feature scaler used during training
├── requirements.txt              # Project dependencies
├── .gitignore                    # Files to ignore (e.g., venv, __pycache__)
└── README.md                     # Project documentation
