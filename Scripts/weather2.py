import requests
import json
from datetime import datetime, timedelta


def get():
    print("-GETTING CURRENT WEATHER")

    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=28.6667&lon=77.2167&units=metric&' \
          'appid=87778270f2de329e6f7d1f021bdead58'

    response = requests.get(url)
    response_json = response.json()

    sunrise = (datetime.utcfromtimestamp(response_json['current']['sunrise']) + timedelta(hours=1))
    sunset = (datetime.utcfromtimestamp(response_json['current']['sunset']) + timedelta(hours=1))
    sunrise = sunrise.strftime('%X')
    sunset = sunset.strftime('%X')

    class Weather:
        def __init__(self, day, temp, icon):
            self.day = day
            self.temp = temp
            self.icon = icon

    weather_list = []

    for x in response_json['daily']:
        weather_list.append(Weather(datetime.utcfromtimestamp(x['dt'])
                                    .strftime('%a'), int(x['temp']['day']), x['weather'][0]['icon']))

    return [weather_list, sunrise, sunset]