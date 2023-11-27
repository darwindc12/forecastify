# Forecastify Weather App

Forecastify is a weather forecasting application built using Streamlit and OpenWeatherMap API to provide weather forecasts for different locations.

## Features

- **Weather Forecast:** Get weather forecasts for up to 5 days.
- **Temperature & Sky Conditions:** View temperature or sky conditions for the chosen location.
- **Visual Representation:** Displays weather data using Plotly for temperature and images for sky conditions.

## Usage

1. **Installation:**

    ```
    pip install -r requirements.txt
    ```

2. **Run the app:**

    ```
    streamlit run app.py
    ```

3. **Input:**

    - Enter the location in the text input field.
    - Use the slider to select the number of days (1 to 5) for the forecast.
    - Choose between viewing temperature or sky conditions using the select box.

4. **Output:**

    - Displays weather forecast data according to the chosen parameters.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/Forecastify.git
    cd Forecastify
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up OpenWeatherMap API:

    - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
    - Add your API key to the `API_KEY` variable in `APIaccess.py`.

## Tech Stack

- Streamlit
- Plotly
- Python Requests
- OpenWeatherMap API

