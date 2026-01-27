import joblib
import pandas as pd

try:
    model = joblib.load('student_performance_predictor.joblib')
    print("Model loaded successfully")
    print("Model type:", type(model))
    if hasattr(model, 'n_features_in_'):
        print("Number of features:", model.n_features_in_)
    if hasattr(model, 'feature_names_in_'):
        print("Feature names:", model.feature_names_in_)
    else:
        print("Feature names not found in model.")
except Exception as e:
    print("Error:", e)
