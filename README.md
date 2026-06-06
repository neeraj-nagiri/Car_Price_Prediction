# Car Price Prediction System

## Project Overview

This project predicts the selling price of a used car using Machine Learning.

The application follows a complete end-to-end workflow:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Pipeline
* Model Serialization
* FastAPI Backend
* Streamlit Frontend
* Cloud Deployment

The model used for prediction is **Linear Regression**.

---

## Project Architecture

User → Streamlit Frontend → FastAPI Backend → Machine Learning Pipeline → Prediction

---

## Features Used

### Numerical Features

* year
* km_driven
* seats
* Mileage
* Engine (CC)
* max_power (in bph)

### Categorical Features

* name
* fuel
* seller_type
* transmission
* owner
* Mileage Unit

---

## Machine Learning Pipeline

The pipeline consists of:

### Numerical Processing

* StandardScaler

### Categorical Processing

* OneHotEncoder

### Model

* Linear Regression

---

## Project Structure

```text
CAR_PRICE_PREDICTION/

├── backend/
│   ├── app.py
│   ├── pydantic_model.py
│   └── car_price_prediction_pipeline.pkl
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements_backend.txt
├── requirements_frontend.txt
└── README.md
```

---

## Model Performance

* R² Score: 0.706
* MAE: 87,180
* RMSE: 114,204

---

## Backend Setup

Install dependencies:

```bash
pip install -r requirements_backend.txt
```

Run FastAPI:

```bash
uvicorn app:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Install dependencies:

```bash
pip install -r requirements_frontend.txt
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Streamlit
* Joblib

---

## Future Improvements

* Add more training data
* Hyperparameter tuning
* Feature selection
* Multiple regression models
* Docker deployment
* CI/CD integration

---

## Author

Neeraj Nagiri

B.Tech Artificial Intelligence & Machine Learning
