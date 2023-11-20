import requests


API_KEY = "3e49e33d4cfc8c559dbf4a86a964d2c1"
URL = "https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"


def get_data(place, forecast_days=None):
    params = {"place": place, "API_KEY": API_KEY}
    response = requests.get(URL.format(**params))
    data = response.json()
    number_values = 8 * forecast_days
    filtered_data = data['list'][0:number_values]
    return filtered_data


