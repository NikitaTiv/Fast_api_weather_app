import pytest
from settings_box.settings import API_KEY
import requests
from typing import Union

@pytest.fixture
def moscow_weather():
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params: dict[str, Union[float, str]] = {
        'lat': 55.7504461,
        'lon': 37.6174943,
        'appid': API_KEY,
        'units': 'metric',
    }
    result = requests.get(weather_url, params=params)
    return result.json()['main']['temp']