import datetime
import time
import requests
from apiKey import apiKey
from dbconfig import dbconfig,_SQL
from DatabaseContextManager import UseDatabase

class DataGatherer:
    def __init__(self,city,units,apiKey):
        self.cityName = city
        self.units = units
        self.apiKey = apiKey
    
    def gather_data(self)->dict:
        fullAddress = f'http://api.openweathermap.org/data/2.5/weather?q={self.cityName}&units={self.units}&appid={self.apiKey}'
        data = requests.get(fullAddress).json()
        return data

class Weather:
    def __init__(self,data:dict):
        self.description = data['weather'][0]['description']
        self.currentTemp = data['main']['temp']
        self.feelsLikeTemp = data['main']['feels_like']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.windSpeed = data['wind']['speed']
       
def console_log_weather_data():
    print('{:d}:{:02d}\n'.format(currentTime.hour, currentTime.minute))
    print(f'{currentTime.date()} | {currentTime.time()}  | -> H:{currentTime.hour}|M:{currentTime.minute}')
    print(f'City:{DG.cityName} | Desc:{WD.description}, CurrT:{WD.currentTemp}, FLT:{WD.feelsLikeTemp}, Range:{WD.temp_min} to {WD.temp_max}, Press:{WD.pressure}, Hum:{WD.humidity}, Wind:{WD.windSpeed}\n')

def db_log_weather_data(DG,WD):
    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL,(DG.cityName,WD.description,WD.currentTemp,WD.feelsLikeTemp,WD.temp_min,WD.temp_max,WD.pressure,WD.humidity,WD.windSpeed,))

DG = DataGatherer('Tczew','metric',apiKey)

while True:

    data = DG.gather_data()
    WD = Weather(data)
    currentTime = datetime.datetime.now()

    if currentTime.minute == 0:
        
        data = DG.gather_data()
        WD = Weather(data)

        db_log_weather_data(DG,WD)
        console_log_weather_data()
    else:
        console_log_weather_data()

    time.sleep(60)