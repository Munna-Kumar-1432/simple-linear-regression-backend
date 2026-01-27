# 🎓 Student Performance Predictor

A modern full-stack web application that predicts a student's test score based on their study hours using a **Linear Regression** machine learning model.

![Project Preview](https://img.shields.io/badge/Machine_Learning-Linear_Regression-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![Frontend](https://img.shields.io/badge/Frontend-Next.js-black)

---

## 🚀 Overview

Ye project ek Simple Linear Regression model pr based hai jo predict krta hai ki user (student) kitne hours padhai krke kitna score achieve kr skta hai. Isme ek powerful FastAPI backend hai aur ek stunning Next.js frontend visualization ke liye.

### **Features**
- **Real-time Prediction:** Input hours and get instant score prediction.
- **Machine Learning Integration:** Uses a pre-trained scikit-learn model.
- **Interactive UI:** Built with Next.js and Tailwind CSS for a premium look.
- **Data Visualization:** Score trends visual presentation (using Recharts).
- **Responsive Design:** Optimized for all screen sizes.

---

## 🏗️ Project Structure

```text
LinearRegression/
├── backend/            # Python FastAPI Server & ML Model
│   ├── main.py         # API Endpoints
│   ├── student_performance_predictor.joblib  # Trained Model
│   └── requirements.txt # Python dependencies
└── frontend/           # Next.js React Application
    ├── src/            # Application logic and UI
    └── package.json    # Node.js dependencies
```

---

## 🛠️ Tech Stack

- **ML Model:** Scikit-learn (Linear Regression)
- **Backend:** FastAPI (Python)
- **Frontend:** Next.js (TypeScript), Tailwind CSS, Lucide Icons, Recharts
- **Deployment Ready:** Configured for local and production environments.

---

## 🚦 How to Run the Project

Follow these steps to get the project up and running locally.

### 1. **Backend Setup**
Navigate to the backend folder and set up a virtual environment.

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
python main.py
```
*Backend will be running on: `http://localhost:8000`*

### 2. **Frontend Setup**
Open a new terminal, navigate to the frontend folder.

```bash
cd frontend
npm install
npm run dev
```
*Frontend will be running on: `http://localhost:3000`*

---

## 🧠 How it Works?

1. **User Input:** User enter krta hai number of study hours (e.g., 5.5 hours).
2. **API Call:** Frontend se request backend API (`/predict`) pr jati hai.
3. **Model Prediction:** Backend me load kiya gaya `Linear Regression` model input data ko process krta hai using the formula `Y = mX + c` (Score = Slope * Hours + Intercept).
4. **Result:** Backend score return krta hai aur frontend use beautiful UI me display krta hai.

---

## 📝 Author
Created with ❤️ by **Er Munna Kumar** for project demonstration.
