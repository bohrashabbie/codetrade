import requests
class get_weather_info:
    def __init__(self):
        self.city = input("enter the city")
        self.humidity = 'None'
        self.tempreture = 'None'
        self.wind_speed = 'None'
        self.pressure = 'None'
        self.response = 'None'
        self.parse_data = 'None'
    def get_info(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=%7B{self.city}%7D&appid=59800ef702cbdd4b0b4949f955e24f7f&units=metric").text
        parse_data = eval(response)
        self.country = self.parse_data['sys']['country']
        if self.country == "IN":
            main_data = parse_data.get('main', {})
            wind_data = parse_data.get('wind', {})
            self.humidity = main_data.get('humidity', 'None')
            self.tempreture = main_data.get('tempreture', 'None')
            self.pressure = main_data.get('pressure', 'None')
            self.wind_speed = wind_data.get('speed', 'None')
        print(self.humidity)
if __name__ == "__main__":
    object = get_weather_info()
    object.get_info()
        