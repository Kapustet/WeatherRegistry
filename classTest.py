import requests
from DatabaseContextManager import UseDatabase
from apiKey import apiKey

class DataGatherer:
    def __init__(self,city,units,apiKey):
        self.cityName = city
        self.units = units
        self.apiKey = apiKey
    
    def gatherData(self)->dict:
        fullAddress = f'http://api.openweathermap.org/data/2.5/weather?q={self.cityName}&units={self.units}&appid={self.apiKey}'
        data = requests.get(fullAddress).json()
        return data

class Weather:
    def __init__(self,data):
        self.description = data['weather'][0]['description']
        self.currentTemp = data['main']['temp']
        self.feelsLikeTemp = data['main']['feels_like']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.windSpeed = data['wind']['speed']

def logWeatherData(data):
    pass



DG = DataGatherer('Tczew','metric',apiKey)

data = DG.gatherData()

WD = Weather(data)


