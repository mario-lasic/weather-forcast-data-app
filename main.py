import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days",min_value=1, max_value=5,help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    #Get data
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
        # Create a temperature plot
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky]
            # Number of columns
            num_cols = 8

            # Iterate over the images and display them in rows with 8 columns each
            for i in range(0, len(image_path), num_cols):
                cols = st.columns(num_cols)
                for col, img in zip(cols, image_path[i:i+num_cols]):
                    col.image(img, use_container_width=True)
    except KeyError:
        st.text(f"{place} does not exists.")

    


