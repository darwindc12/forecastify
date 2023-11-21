# Define the API key for accessing the OpenWeatherMap API
API_KEY = "76df065c44fd5994d2e9424a48fd90f4"

# Define a function to retrieve weather data for a specified place and number of days
def get_data(place, day=None, view_by=None):
    # Construct the URL for the OpenWeatherMap API request with the provided place and API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    return url