from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="ML Model API")

# Dummy trained model (replace with your own model)
class SimpleModel:
    def predict(self, X):
        return ["Positive" if x[0] > 0.5 else "Negative" for x in X]

model = SimpleModel()

# Input schema
class InputData(BaseModel):
    value: float

@app.get("/")
def root():
    return {"message": "✅ FastAPI ML Model is Running!"}

@app.post("/predict/")
def predict(data: InputData):
    input_value = np.array([[data.value]])
    prediction = model.predict(input_value)
    return {"prediction": prediction[0]}
