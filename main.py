import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("City: ")

days = st.slider("Forecast Days: ", 1, 5, help="Select the number of days")
data = st.selectbox("Select data to view: ", ("Temperature", "Sky"))

st.subheader(f"{data} for the next {days} days in {place}")