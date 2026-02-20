import streamlit as st
import joblib

st.title("Adaptive Traffic Management System")

st.subheader("Traffic Video")
video = open("videos/traffic-2.mp4", "rb")
st.video(video.read())

model = joblib.load("models/traffic_model.pkl")

vehicles = st.slider("Select number of vehicles detected", 0, 200, 50)

prediction = model.predict([[vehicles]])

st.success(f"Green signal time: {int(prediction[0])} seconds")