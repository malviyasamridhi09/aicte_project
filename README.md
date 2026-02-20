# 🚦 Adaptive Traffic Management System using Machine Learning

## 📌 Overview
The Adaptive Traffic Management System is a Machine Learning–based project that dynamically predicts the optimal traffic signal green time based on vehicle density. Unlike traditional fixed-timer signals, this system adjusts signal timing intelligently to reduce traffic congestion and improve traffic flow efficiency.

This project includes a Streamlit web interface, a trained Machine Learning model, and traffic video integration for realistic simulation.

---

## 🎯 Objectives
- Reduce traffic congestion using adaptive signal timing
- Predict green signal duration based on vehicle count
- Demonstrate real-world application of Machine Learning
- Provide an interactive user interface using Streamlit

---

## 🧠 Machine Learning Model
- Model Used: Linear Regression
- Input: Number of vehicles
- Output: Predicted green signal time (seconds)
- Library: Scikit-learn

---

## 🖥️ Features
- 🎥 Traffic video display for simulation
- 🎚️ Interactive slider to adjust vehicle density
- 🤖 Machine Learning prediction of signal timing
- 🌐 User-friendly Streamlit web interface
- 📦 Lightweight and GitHub-ready project structure

---

## 🛠️ Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Git & GitHub

---

## 📁 Project Structure

adaptive-traffic-system/
│
├── app.py # Streamlit web application
├── train_model.py # Model training script
├── requirements.txt # Required libraries
├── README.md # Project documentation
├── .gitignore # Ignore unnecessary files
│
├── data/
│ └── traffic.csv # Dataset
│
├── models/
│ └── traffic_model.pkl # Trained ML model
│
└── videos/
└── traffic-2.mp4 # Traffic simulation video
