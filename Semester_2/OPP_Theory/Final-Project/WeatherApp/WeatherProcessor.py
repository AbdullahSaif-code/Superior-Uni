from WeatherFetcher import WeatherFetcher

class WeatherProcessor(WeatherFetcher):
    def __init__(self, api_key):
        super().__init__(api_key)

    def process_weather(self, city):
        weather_data = self.fetch_weather(city)
        if weather_data:
            # Process weather data
            weather = weather_data['weather'][0]['main']
            temp_c = round((weather_data['main']['temp'] - 32) * 5 / 9, 2)
            min_temp_c = round((weather_data['main']['feels_like'] - 32) * 5 / 9, 2)
            max_temp_c = round((weather_data['main']['temp_max'] - 32) * 5 / 9, 2)
            humidity = weather_data['main']['humidity']
            return {
                "city": city,
                "weather": weather,
                "temp_c": temp_c,
                "min_temp_c": min_temp_c,
                "max_temp_c": max_temp_c,
                "humidity": humidity
            }
        return None
