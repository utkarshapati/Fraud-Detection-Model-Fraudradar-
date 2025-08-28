import streamlit as st
import pandas as pd
import joblib

model =joblib.load("fraud_detection_pipeline.pkl")
st.title("Task of fraud detection application")
st.markdown("Enter the transaction and use button down to predict")
st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount here", min_value=0.0,value=1000.0)
oldbalanceOrg= st.number_input("Old balance here(Sender)",min_value=0.0 , value=1000.0)
newbalanceOrig =st.number_input("New balance here (sender)",min_value=0.0 , value=9000.0)
oldbalanceDest = st.number_input("old balance here (reciever)",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("new balance here (reciever)",min_value=0.0,value=0.0)

if st.button("Predict the fraud"):
    input_data =pd.DataFrame([{
        "type": transcation_type,
        "amount": amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction:'{int(prediction)}'")
    
    if prediction ==1:
        st.error("This can be fraud")
    else:
        st.success("This transcation looks like is not a fraud transcation")