import streamlit as st

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