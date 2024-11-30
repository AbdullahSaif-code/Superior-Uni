from WeatherProcessor import WeatherProcessor
from FileHandler import FileHandler

class MenuHandler:
    def __init__(self, api_key):
        self.__processor = WeatherProcessor(api_key)

    def display_menu(self):
        while True:
            print("\nWeather App Menu:")
            print("1. Search Weather")
            print("2. Open CSV File")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                city = input("Enter the city name: ")
                weather = self.__processor.process_weather(city)
                if weather:
                    print("\nWeather Details:")
                    for key, value in weather.items():
                        print(f"{key.capitalize()}: {value}")
                    FileHandler.save_to_csv(weather)
                    print("Weather data saved to CSV.")
            elif choice == "2":
                FileHandler.open_csv()
            elif choice == "3":
                print("Exiting the Weather App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
