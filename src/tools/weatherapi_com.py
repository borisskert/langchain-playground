import os
import urllib.request
from typing import Any

from langchain_core.tools import tool


@tool(
    "get_weather",
    description="Get the weather for a given city")
def get_weather(city: str) -> Any:
    apikey = os.environ.get("WEATHER_API_KEY")
    encoded_city = urllib.parse.quote(city)

    response = urllib.request.urlopen(f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={encoded_city}&aqi=no")

    if response.getcode() != 200:
        raise Exception("Error fetching weather data")

    return response.read()
