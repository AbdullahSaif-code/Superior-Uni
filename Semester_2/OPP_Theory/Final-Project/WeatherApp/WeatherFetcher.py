import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.__api_key = api_key

    def fetch_weather(self, city):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={self.__api_key}")
        if response.status_code == 200:
            return response.json()
        else:
            print("City not found or API error.")
            return None
