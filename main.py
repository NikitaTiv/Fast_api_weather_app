from fastapi import FastAPI

from settings_box.config import API_KEY
from utils import get_weather

app = FastAPI()


@app.get('/weather/{city_name}')
def read_item(city_name: str):
    """Show temperature."""
    temperature = get_weather(city_name, API_KEY)
    return {'city': city_name, 'temp': temperature}
