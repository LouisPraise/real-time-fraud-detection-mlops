from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

Model = joblib.load("My_Fd_Model.pkl")

@app.get("/")
def home():
    return {"Data": "My Fraud Detection API is up and running!"}

@app.post("/predict")
def predict(transaction: dict):
    features = np.array(list(transaction.values())).reshape(1, -1)
    prediction = Model.predict(features),
    probability = Model.predict_proba(features)[0][1]
    return {
        "fraud": bool(prediction[0]),
        "probability": round(float(probability), 4)
        }