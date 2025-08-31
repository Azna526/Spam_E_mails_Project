import streamlit as st
import joblib

# Load the trained model
model = joblib.load("spam_pipeline.joblib")

st.title("📧 Spam Email Classifier")

# Input box
message = st.text_area("Enter your email/message:")

if st.button("Predict"):
    prediction = model.predict([message])

    if prediction[0] == "ham":
        st.success("✅ This email is NOT Spam (Ham).")
    else:
        st.error("🚨 This email is Spam!")
