import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Sorry, I couldn't find that city."

    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    report = (
        f"The weather in {city} is {description}. "
        f"The temperature is {temperature} degrees Celsius. "
        f"It feels like {feels_like} degrees. "
        f"The humidity is {humidity} percent."
    )

    return report