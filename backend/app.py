from fastapi import FastAPI
from pydantic_model import CarData
import joblib
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

pipeline = joblib.load(BASE_DIR/"Car_price_prediction_pipeline.pkl")

app = FastAPI()

@app.get("/")
def home():
    return "Car Price Prediction API is running"

@app.post("/predict")
def predict(car:CarData):
    new_car = pd.DataFrame({
        "name": [car.name],
        "fuel": [car.fuel],
        "seller_type": [car.seller_type],
        "transmission": [car.transmission],
        "owner": [car.owner],
        "year": [car.year],
        "km_driven": [car.km_driven],
        "seats": [car.seats],
        "Mileage": [car.Mileage],
        "Engine (CC)": [car.Engine_CC],
        "max_power (in bph)": [car.max_power_bph],
        "Mileage Unit": [car.Mileage_Unit]
    
    })

    prediction = pipeline.predict(new_car)

    return {
        "Prediction Price" : round(float(prediction[0]),2)
    }




