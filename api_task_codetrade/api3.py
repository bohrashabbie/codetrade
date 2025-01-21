import requests
import re
import csv
class GetWeatherInfo:
    """ this is use to get the weather information"""
    def __init__(self):
        self.city = input("please enter city name")
        self.humidity = 'None'
        self.temperature = 'None'
        self.wind_speed = 'None'
        self.pressure = 'None'
        self.response = 'None'
        self.parse_data = 'None'
    def get_info(self):  

        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=59800ef702cbdd4b0b4949f955e24f7f&units=metric")
            response_Api = response.text
            parse_data = eval(response_Api)
            # print(parse_data)
            if parse_data.get('cod') == 200:  # Check if the city was found
                self.country = parse_data['sys']['country']
                if self.country == "IN":  # Check if the country is India
                    other_data = parse_data.get('main', {})
                    wind_data = parse_data.get('wind', {})
                    
                    # Assign the weather data
                    self.humidity = other_data.get('humidity', 'None')
                    self.temperature = other_data.get('temp', 'None')
                    self.pressure = other_data.get('pressure', 'None')
                    self.wind_speed = wind_data.get('speed', 'None')
                    self.store_to_csv()
                    
                else:
                    print(f"the country you have entered have no existence in this api")
        except Exception as e:
            print(f"error occurred during execution{e}")
        print(self.humidity,"\n", self.temperature, self.pressure, self.wind_speed)
            
    def validate_city(self,city):
        exp = "^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$"
        return re.fullmatch(exp, city)
    def store_to_csv(self):
        """
        Initializes the CSV file with a header if it doesn't already exist or is empty.
        """
        try:
            with open("weatherfiles.csv", 'w', newline='') as file:
                reader = csv.reader(file)
                if not any(reader):
                    file.write("city_name", "tempreture", "pressure", "wind_speed")
                file.write(self.city, self.temperature, self.pressure, self.wind_speed)
        except (FileNotFoundError, csv.Error):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["first_name", "middle_name", "last_name", "email_id", "password", "contact_number", "user_name", "is_admin"])

if __name__ == "__main__":
    weather_info = GetWeatherInfo()
    weather_info.get_info()
