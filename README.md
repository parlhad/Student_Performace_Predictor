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


---

## 📌 Usage Instructions

To get a prediction, follow these steps in the interactive web interface:

1.  **Enter Hours Studied:** Input the total number of hours spent studying.
2.  **Enter Previous Exam Score:** Provide the score obtained in the last assessment.
3.  **Enter Papers Practiced:** Input the count of sample question papers completed.
4.  **Enter Daily Sleep Hours:** Specify the average amount of sleep per day.
5.  **Click "Predict Performance":** The system will process the data through the trained model.

> **Result:** The application calculates and displays the
>  **Predicted Performance Index** instantly on the screen.



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

## 📌 Project 
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
```
---

## 🛠️ Built With

| Technology | Purpose |
|----------|--------|
| Python | Core programming language |
| scikit-learn | Model training and evaluation |
| joblib | Model & scaler serialization |
| Streamlit | Web application deployment |
| Pandas | Data handling |
| NumPy | Numerical computations |

---

## 🧠 How It Works

### 1️⃣ Data Collection
The dataset contains the following features:
- **Hours Studied**
- **Previous Exam Scores**
- **Sample Question Papers Practiced**
- **Daily Sleep Hours**

---

### 2️⃣ Preprocessing
- Feature scaling using `StandardScaler`
- Ensures consistent numeric input during prediction

---

### 3️⃣ Model Training
- Regression-based machine learning model
- Trained using scikit-learn
- Optimized for performance prediction

---

### 4️⃣ Model Serialization
- Model and scaler saved using `joblib`
- Enables reuse without retraining

---

### 5️⃣ Deployment
- Streamlit-based interactive web application
- Accepts real-time user input
- Applies preprocessing
- Displays predicted performance score instantly

---

## 📥 Getting Started (Local Setup)

Follow these steps to run the project locally.

### 🔽 Clone the Repository
```bash
git clone https://github.com/parlhad/Student_Performace_Predictor.git
cd Student_Performace_Predictor

## install requerments

python -m pip install -r requirements.txt


## run on terminal

python -m streamlit run app.py

---
## 🧑‍💻 Why This Project Matters

This project is a strong portfolio piece because it:

✔ Demonstrates a clear understanding of the complete Machine Learning pipeline  
✔ Solves a real-world educational prediction problem  
✔ Applies model serialization and real-time deployment techniques  
✔ Uses a modern, interactive web interface  
✔ Is resume-ready and recruiter-friendly  

---

## 📈 Future Improvements

Possible enhancements include:

✨ Advanced data visualizations and insights  
✨ CSV upload support for batch predictions  
✨ Multiple model comparison and evaluation  
✨ Performance analytics dashboard  
✨ Cloud-based logging of prediction history  

---

## 🤝 Contributing

Contributions, feedback, and improvements are welcome.  
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is **open-source** — you are free to adapt, modify, and enhance it with proper attribution.

---

## 👤 Author

**Pralhad Balaji Jadhav**  
📍 Nanded, Maharashtra, India  

🌐 GitHub: https://github.com/parlhad  
📧 Email: *(parlhadjadhav7@gmail.come)*



## ⭐ Final Note

This project reflects a complete **end-to-end Machine Learning workflow**, covering data preprocessing, model training, serialization, and deployment through a modern web interface.

It demonstrates practical problem-solving skills, real-world ML deployment experience, and the ability to build clean, user-focused applications — making it a strong portfolio project for **internships, entry-level roles, and academic evaluations**.

If you find this project useful or insightful, feel free to ⭐ star the repository and share your feedback.

---



