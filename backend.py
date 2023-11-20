import requests
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("API_KEY")

# URL for OpenWeatherMap API
URL = "https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"


def get_data(place, forecast_days=None):
    """
    Get weather forecast data for a specific place.

    Args:
        place (str): The name of the place for which to get the weather forecast.
        forecast_days (int, optional): The number of forecast days to retrieve. Defaults to None.

    Returns:
        list: A list of forecast data for the specified place.
    """
    # Set parameters for the API request
    params = {"place": place, "API_KEY": API_KEY}

    # Send GET request to the OpenWeatherMap API
    response = requests.get(URL.format(**params))

    # Parse the response as JSON
    data = response.json()

    # Calculate the number of values to retrieve based on the forecast days
    number_values = 8 * forecast_days

    # Filter the data to retrieve only the specified number of values
    filtered_data = data['list'][0:number_values]

    return filtered_data