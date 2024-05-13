import requests
from logs import logger
import config as cfg

class getWeather():
    def __init__(self, zip):
        # load confiugration
        self.config = cfg.get_config()
        self.zip = zip
        # self.error = None
        self.weather = self.get_weather()
        del self.weather['Credits']
        del self.weather['Code']
        logger.info(f'Weather for {self.zip} retrieved')
        
        
    def get_weather(self):
        logger.debug(f'Getting weather for {self.zip}')
        querystring = {"zip":self.zip}
        headers = {
            "X-RapidAPI-Key": self.config['weather_api']['rapidapi_key'],
            "X-RapidAPI-Host": self.config['weather_api']['rapidapi_host']
        }
        response = requests.get(self.config['weather_api']['url'], headers=headers, params=querystring)
        if response.status_code == 404:
            self.error = "Invalid Zip Code"
            return None
        return response.json()

    def humidity_level(self):
        logger.debug(f'Humidity requested for {self.zip}')
        return f'Humidity is {self.weather["RelativeHumidity"]} %'

    def temperature(self):
        logger.debug(f'Temperature requested for {self.zip}')
        return f'Temperature is {self.weather["TempF"]} degrees Fahrenheit'

    def verbal_weather(self):
        message = f'Weather is {self.weather["Weather"]} and a temperature is {self.weather["TempF"]} degrees Fahrenheit'
        logger.debug(f'Verbose message requested for {self.zip}')
        logger.debug(message)
        return message
    
    def weather_report(self):
        return self.weather


