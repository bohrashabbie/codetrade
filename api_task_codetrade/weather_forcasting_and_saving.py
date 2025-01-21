import requests
import re
import csv
class GetWeatherInfo:
    """ this is used to get the weather information """
    def __init__(self):
        self.humidity = 'None'
        self.temperature = 'None'
        self.wind_speed = 'None'
        self.pressure = 'None'
        self.response = 'None'
        self.parse_data = 'None'
    
    def get_info(self): 
        # validate the city name before processing
        while True:
            self.city = input("enter your city name : ")
            if  self.validate_city(self.city):
                break
            print("Invalid city name format.")
        
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=59800ef702cbdd4b0b4949f955e24f7f&units=metric")
            response_Api = response.text
            print(response_Api)
            parse_data = eval(response_Api)
            if parse_data.get('cod') == 200:  # check if the city was found
                self.country = parse_data['sys']['country']
                
                if self.country == "IN":  # check if the country is India
                    other_data = parse_data.get('main', {})
                    wind_data = parse_data.get('wind', {})
                    
                    # assign the weather data
                    self.humidity = other_data.get('humidity', 'None')
                    self.temperature = other_data.get('temp', 'None')
                    self.pressure = other_data.get('pressure', 'None')
                    self.wind_speed = wind_data.get('speed', 'None')
                    self.store_to_csv()  # Storing data to csv
                    
                    return f"City: {self.city}, Temperature: {self.temperature}, Pressure: {self.pressure}, Wind Speed: {self.wind_speed}"
                else:
                    print(f"The country '{self.country}' is not supported by this API.")
            else:
                print("City not found or invalid")
        
        except Exception as e:
            print(f"Error occurred during execution: {e}")
            
    def validate_city(self, city):
        """ Validate city name using regular expression """
        exp = "^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$"
        return re.fullmatch(exp, city) is not None
    
    def store_to_csv(self):
        """ Initializes the CSV file with a header if it doesn't already exist or is empty. """
        try:
            file_exists = False
            
            try:
                with open("weatherfiles.csv", 'r', newline='') as file:
                    reader = csv.reader(file)
                    file_exists = any(reader)  # If the file is not empty, file_exists becomes True
            except FileNotFoundError:
                pass  
            with open("weatherfiles.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["city_name", "temperature", "pressure", "wind_speed", "humidity"])
                writer.writerow([self.city, self.temperature, self.pressure, self.wind_speed, self.humidity])

        except Exception as e:
            print(f"Error occurred while writing to CSV: {str(e)}")

if __name__ == "__main__":
    """
    this is the main file to 
        """
    weather_info = GetWeatherInfo()
    weather_info.get_info()
