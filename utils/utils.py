import requests
from settings_box.settings import API_KEY
from typing import Union


def get_coord(city: str) -> tuple[float, float]:
    """Запрашивает на сайте погоды координаты по названию города."""
    coord_url = 'http://api.openweathermap.org/geo/1.0/direct'
    params: dict[str, str] = {
        'appid': API_KEY,
        'q': city,
    }
    result = requests.get(coord_url, params=params)
    return result.json()[0]['lat'], result.json()[0]['lon']


def get_weather(latitude: float, longitude: float) -> float:
    """Запрашивает на сайте погоды температуру по геокоординатам."""
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params: dict[str, Union[float, str]] = {
        'lat': latitude,
        'lon': longitude,
        'appid': API_KEY,
        'units': 'metric',
    }
    result = requests.get(weather_url, params=params)
    return result.json()['main']['temp']
