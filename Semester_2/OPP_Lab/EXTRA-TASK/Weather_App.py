import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input(f"\nEnter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# print(weather_data.status_code)    # return 200 if Api working and 404 if not working

# print(weather_data.json())         # return the all data from Api

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = (weather_data.json()['main']['temp'])
    min_temp = (weather_data.json()['main']['feels_like'])
    max_temp = round(weather_data.json()['main']['temp_max'])
    humidity = round(weather_data.json()['main']['humidity'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {(temp-32)*0.5}ºc")
    print(f"The minimum temperature in {user_input} is: {(min_temp-32)*0.5}ºc")
    print(f"The maximum temperature in {user_input} is: {(max_temp-32)*0.5}ºc")
    print(f"The humidity in {user_input} is: {humidity}%")