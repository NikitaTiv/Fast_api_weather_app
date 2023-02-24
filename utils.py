import requests
from typing import Union


def get_weather(city: str, api_key: str) -> float | None:
    """Запрашивает на сайте погоды температуру."""
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params: dict[str, Union[float, str]] = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    result = requests.get(weather_url, params=params)
    if not result:
        return None
    return result.json()['main']['temp']
