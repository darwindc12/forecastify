import streamlit as st
from APIaccess import get_data
import plotly.express as px

# Set the title for the Streamlit app
st.title("Forecastify")
st.write("Weather Forecast for the Next Days")

# Create a text input field for the user to enter the place
place = st.text_input("Place")

# Create a slider for the user to select the number of forecast days (1 to 5 days)
day = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Slider to select the number of days to forecast.")

# Create a selectbox for the user to choose between viewing temperature or sky conditions
view_by = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Display a subheader indicating the chosen view, number of days, and place
st.subheader(f"{view_by} for the next {day} days in {place}")

# Create a selectbox for the user to choose between viewing temperature or sky conditions
view_by = st.selectbox("Select data to view", ("Temperature",))

# Check if the user has entered a place
if place:
    # Attempt to get filtered weather data based on the user's input place and number of forecast days

    try:
        filtered_data = get_data(place, day)

        # Check if the user chose to view temperature data
        if view_by == "Temperature":
            # Extract temperature data and dates from the filtered data
            temperature = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]

            # Create a line chart using Plotly with temperature data and dates
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature(c)"})

            # Display the line chart in the Streamlit app
            st.plotly_chart(figure)

    # Handle the KeyError exception, which is raised if the 'place' does not exist in the API response
    except KeyError:
        # Display a message using Streamlit indicating that the specified place does not exist
        st.write("Place does not exists")