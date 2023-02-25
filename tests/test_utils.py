from utils import get_weather
from settings_box.config import API_KEY


def test_get_weather(moscow_weather):
    assert get_weather('Moscow', API_KEY) == moscow_weather
