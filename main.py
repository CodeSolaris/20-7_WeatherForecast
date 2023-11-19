import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("City: ")

days = st.slider("Forecast Days: ", 1, 5, help="Select the number of days")
data = st.selectbox("Select data to view: ", ("Temperature", "Sky"))

st.subheader(f"{data} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-07-24", "2022-07-25", "2022-07-26", "2022-07-27"]
    temp = [20, 21, 22, 23]
    temps = [days * i for i in temp]
    return dates, temps


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (°C)'})
st.plotly_chart(figure)
