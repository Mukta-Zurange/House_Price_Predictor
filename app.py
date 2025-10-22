import streamlit as st
import joblib

model_multi = joblib.load('model.pkl')

st.title("🏡 House Price Prediction App")
st.write("Enter the details below to estimate the house price:")

# --- Input fields ---
area = st.number_input("Area (in sq. ft):", min_value=500.0, max_value=10000.0, value=2000.0, step=100.0)
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms:", min_value=1, max_value=10, value=2)
stories = st.number_input("Number of Stories:", min_value=1, max_value=4, value=2)

mainroad = st.selectbox("Main Road:", ["Yes", "No"])
guestroom = st.selectbox("Guest Room:", ["Yes", "No"])
basement = st.selectbox("Basement:", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating:", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning:", ["Yes", "No"])
parking = st.number_input("Parking (number):", min_value=0, max_value=5, value=1)
prefarea = st.selectbox("Preferred Area:", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing Status:", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Convert categorical inputs to numeric
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0
furnishing_map = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}
furnishingstatus = furnishing_map[furnishingstatus]

# --- Predict Button ---
if st.button("🔮 Predict Price"):
    X = [[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
           hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]]
    
    predicted_price = model_multi.predict(X)[0]
    st.success(f"🏠 Predicted House Price: ₹{predicted_price:,.2f}")
