import requests
from infos import WEATHER_API_KEY
import datetime


class Weather:
    def __init__(self, WEATHER_API_KEY, frequency=30):
        self.WEATHER_API_KEY = WEATHER_API_KEY
        self.frequency = frequency
        self.weather = None
        self.weather_time = datetime.datetime.now()
        self.is_expired = True

    def get_weather(self, CITY):
        weather_expired = (datetime.datetime.now() - self.weather_time >
                           datetime.timedelta(minutes=self.frequency))

        if self.weather_expired:
            return requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={self.WEATHER_API_KEY}'
            )


w = Weather(WEATHER_API_KEY)
w.get_weather("Paris")