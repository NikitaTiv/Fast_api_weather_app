from utils.utils import get_coord, get_weather


def test_get_coord():
    assert get_coord('Moscow') == (55.7504461, 37.6174943)


def test_get_weather(moscow_weather):
    assert get_weather(55.7504461, 37.6174943) == moscow_weather
