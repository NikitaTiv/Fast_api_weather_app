import pytest
from settings_box.config import API_KEY
import requests
from typing import Union

@pytest.fixture
def moscow_weather():
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params: dict[str, Union[float, str]] = {
        'q': 'Moscow',
        'appid': API_KEY,
        'units': 'metric',
    }
    result = requests.get(weather_url, params=params)
    return result.json()['main']['temp']
