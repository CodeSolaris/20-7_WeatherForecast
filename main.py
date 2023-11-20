import streamlit as st
import plotly.express as px
from backend import get_data

place = st.text_input("Place: ")

days = st.slider("Forecast Days: ", 1, 5, help="Select the number of days")
kind = st.selectbox("Select kind to view: ", ("Temperature", "Sky"))
st.subheader(f"{kind} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, forecast_days=days)
        dates = [d["dt_txt"] for d in filtered_data]

        if kind == "Temperature":
            temperatures = [(d["main"]["temp"] - 273.15) for d in filtered_data]
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"}
            )
            st.plotly_chart(figure)
        else:
            weather_condition = [d["weather"][0]["main"] for d in filtered_data]
            images_list = ["images/" + w.lower() + ".png" for w in weather_condition]
            columns = st.columns(4)
            for i, (date, image_path) in enumerate(zip(dates, images_list)):
                column_index = i % 4  # Get the column index based on the current iteration
                column = columns[column_index]
                column.image(image_path, width=110)
                column.text(date)
    except KeyError:
        st.error("City not found, please try again")