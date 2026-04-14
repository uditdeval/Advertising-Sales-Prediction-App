import streamlit as st
import pickle

# model load
model = pickle.load(open('model.pkl', 'rb'))

st.title("Advertising Sales Prediction (India ₹)")

st.write("👉 Enter advertising budget in Indian Rupees (₹)")

# inputs in rupees
tv = st.number_input("Enter TV Budget (in ₹)")
radio = st.number_input("Enter Radio Budget (in ₹)")
newspaper = st.number_input("Enter Newspaper Budget (in ₹)")

if st.button("Predict"):
    
    # 🔥 convert ₹ → dataset format (thousands of dollars)
    tv_model = tv / 80000
    radio_model = radio / 80000
    newspaper_model = newspaper / 80000

    # prediction
    prediction = model.predict([[tv_model, radio_model, newspaper_model]])

    # 🔥 convert output into ₹ (assumption)
    sales_rupees = prediction[0] * 1000

    # show result
    st.success(f"Predicted Sales: ₹{sales_rupees:.2f}")

    # extra info (for clarity)
    st.write("ℹ️ Note: This is an estimated value based on model prediction.")