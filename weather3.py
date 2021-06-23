import os
import sys
import requests
import json
from datetime import datetime


def time_from_utc_with_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

# Enter your API key
api_key = "6a0ee49cc28ca1e1f171a342bb4bef6b"

# Get city name from user
city_name = input("Enter city name : ")

# API url
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

# Get the response from weather url
response = requests.get(weather_url)

weather_data = response.json()

if weather_data['cod'] == 200:
    kelvin = 273.15 # Temperature shown here is in Kelvin and I will show in Celsius
    temp = int(weather_data['main']['temp'] - kelvin)
    feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed'] * 3.6
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    timezone = weather_data['timezone']
    cloudy = weather_data['clouds']['all']
    description = weather_data['weather'][0]['description']

    sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
    sunset_time = time_from_utc_with_timezone(sunset + timezone)

    desktop = os.path.join(os.path.expanduser("~"), "desktop\\weather_info.txt")
    org_stdout = sys.stdout

    with open(desktop, "w") as file:
        for _ in range(2):
            if _==1:
                sys.stdout = file
            print(f"Weather Information for City: {city_name}")
            print(f"Temperature (Celsius): {temp}")
            print(f"Feels like in (Celsius): {feels_like_temp}")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print("Wind speed: {0:.2f} km/hr".format(wind_speed))
            print(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
            print(f"Cloud: {cloudy}%")
            print(f"Info: {description}")
            sys.stdout = org_stdout
else:
    print(f"City Name: {city_name} was not found!")