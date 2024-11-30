import csv
import os

class FileHandler:
    _file_name = "weather_data.csv"

    @staticmethod
    def save_to_csv(data):
        file_exists = os.path.exists(FileHandler._file_name)
        with open(FileHandler._file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["City", "Weather", "Temperature (°C)", "Min Temp (°C)", "Max Temp (°C)", "Humidity (%)"])
            writer.writerow([data["city"], data["weather"], data["temp_c"], data["min_temp_c"], data["max_temp_c"], data["humidity"]])

    @staticmethod
    def open_csv():
        if os.path.exists(FileHandler._file_name):
            os.startfile(FileHandler._file_name)
        else:
            print("No weather data file found.")