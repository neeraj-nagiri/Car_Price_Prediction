import streamlit as st
import requests 

st.title("Car Price Prediction system")

name = st.selectbox(
    "Brand",
    [
        "Maruti","Hyundai","Ford","Tata","Volkswagen","Renault","Toyota","Mahindra","Chevrolet","Honda"
    ]
)

year = st.number_input(
    "year",
    min_value=1990,
    max_value=2030
)

fuel = st.selectbox(
    "Enter the fuel type of your car",
    ["Diesel", "Petrol", "CNG", "LPG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    ["First Owner","Second Owner","Third Owner","Fourth & Above Owner","Test Drive Car"]
)

mileage_unit = st.selectbox(
    "Mileage Unit",
    ["kmpl", "km/kg"]
)

km_driven = st.number_input(
    "KM Driven",
    min_value=0
)

seats = st.number_input(
    "Seats",
    min_value=1,
    max_value=7
)

mileage = st.number_input(
    "Mileage",
    min_value=0.0
)

engine_cc = st.number_input(
    "Engine CC",
    min_value=0.0
)

max_power = st.number_input(
    "Max Power (BHP)",
    min_value=0.0
)

predicted_btn = st.button("predict")
try:

    if predicted_btn:
        data = {
        "name" :name,
        "fuel" : fuel,
        "seller_type" : seller_type,
        "transmission" : transmission,
        "owner" : owner,
        "year" : int(year),
        "km_driven" : int(km_driven),
        "seats" : int(seats),
        "Mileage" : float(mileage),
        "Engine_CC" : float(engine_cc),
        "max_power_bph" : float(max_power),
        "Mileage_Unit" : mileage_unit
        }

        response = requests.post(
            "https://car-price-backend-qess.onrender.com/predict",
            json=data
        )
        if response.status_code==200:

            result = response.json()

            st.success(f"The Predicted Price of your car is:- {result['Prediction Price']}")

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")
