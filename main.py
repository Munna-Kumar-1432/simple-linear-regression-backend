from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Student Performance Predictor API",
    description="API to predict student scores based on hours studied using a Linear Regression model.",
    version="1.0.0"
)

# Add CORS middleware to allow the frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
try:
    model = joblib.load('student_performance_predictor.joblib')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class PredictionRequest(BaseModel):
    hours: float

class PredictionResponse(BaseModel):
    predicted_score: float

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Student Performance Predictor API is running",
        "endpoints": {
            "predict": "/predict (POST)",
            "docs": "/docs (Swagger UI)"
        }
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Machine Learning model NOT found or failed to load.")
    
    try:
        # Prepare input for prediction (2D array expected by sklearn)
        input_data = np.array([[request.hours]])
        prediction = model.predict(input_data)
        
        # Ensure the score is within a logical range (0-100) if applicable, 
        # but returning raw prediction from model as per standard.
        # Use .item() or index carefully to avoid deprecation warnings
        result = float(prediction[0][0]) if len(prediction.shape) > 1 else float(prediction[0])
        
        return PredictionResponse(predicted_score=round(result, 2))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
