import requests
from typing import TypedDict

class Params(TypedDict):
    q: str
    appid: str
    units: str


def get_weather(city: str, api_key: str) -> float | None:
    """Запрашивает на сайте погоды температуру."""
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params: Params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    result = requests.get(weather_url, params=params)
    if not result:
        return None
    return result.json()['main']['temp']
