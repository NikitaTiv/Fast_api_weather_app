from fastapi import FastAPI

from utils.utils import get_coord, get_weather

app = FastAPI()


@app.get('/weather/{city_name}')
def read_item(city_name: str):
    """Show temperature."""
    latitude: float
    longitude: float
    try:
        latitude, longitude = get_coord(city_name)
    except IndexError:
        return 'Введите корректное название города.'
    temperature = get_weather(latitude, longitude)
    return {'city': city_name, 'temp': temperature}
