# Contains information for Weather API.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:  # OK status
        main = data['main']
        weather_info = data['weather'][0]
        temperature = main['temp'] - 273.15  # Convert Kelvin to Celsius
        description = weather_info['description']
        return f"{round(temperature)}°C, {description}"
    else:
        return "Error fetching weather"
