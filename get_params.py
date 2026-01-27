import joblib
import numpy as np

try:
    model = joblib.load('student_performance_predictor.joblib')
    print("Intercept:", model.intercept_)
    print("Coefficients:", model.coef_)
except Exception as e:
    print("Error:", e)
