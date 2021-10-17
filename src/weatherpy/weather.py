import requests
from weatherpy.infos import WEATHER_API_KEY
import datetime
import numpy as np


class Weather:
    def __init__(self, WEATHER_API_KEY, frequency=30):
        self.WEATHER_API_KEY = WEATHER_API_KEY
        self.frequency = frequency
        self.weather = None
        self.weather_time = datetime.datetime.now()

    def update_weather(self, CITY):
        weather_expired = (datetime.datetime.now() - self.weather_time >
                           datetime.timedelta(minutes=self.frequency))

        if weather_expired or self.weather is None:
            self.weather = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={self.WEATHER_API_KEY}&units=metric'
            ).json()

    def get_weather(self, CITY):
        self.update_weather(CITY)
        # we collect the data we want
        wind = self.weather["wind"]["speed"]
        cloudiness = self.weather["clouds"]["all"]
        temperature = self.weather["main"]["temp"]
        humidity = self.weather["main"]["humidity"]

        # we need to normalize them
        # TODO : work with more data to provide better normalization

        # cloudiness and humidity "are" %
        cloudiness /= 100
        humidity /= 100

        # we decide that the t° expressive range is [0, 35]°C
        temperature = np.round(np.clip(temperature / 35, 0, 1), decimals=3)
        # we set wind speed range to [0, 15] m/s
        wind = np.round(np.clip(wind / 15, 0, 1), decimals=3)

        return {
            "temperature": temperature,
            "humidity": humidity,
            "cloudiness": cloudiness,
            "wind": wind
        }


w = Weather(WEATHER_API_KEY)
print(w.get_weather("Paris"))
