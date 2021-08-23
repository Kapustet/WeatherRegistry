import datetime
import time
import requests
from api_key import api_key
from dbconfig import dbconfig,_INSERT_INTO_LOG,_INSERT_INTO_ERROR_LOG
from requests.exceptions import ConnectionError
from database_context_manager import UseDatabase

class DataGatherer:
    def __init__(self,city,units,api_key):
        self.city_name = city
        self.units = units
        self.api_key = api_key
    
    def gather_data(self)->dict:
        full_address = f'http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&units={self.units}&appid={self.api_key}'
        data = requests.get(full_address).json()
        return data

class Weather:
    def __init__(self,data:dict):
        self.description = data['weather'][0]['description']
        self.current_temp = data['main']['temp']
        self.feels_like_temp = data['main']['feels_like']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']
       
def console_log_weather_data():
    print('{:d}:{:02d}\n'.format(current_time.hour, current_time.minute))
    print(f'{current_time.date()} | {current_time.time()}  | -> H:{current_time.hour}|M:{current_time.minute}')
    print(f'City:{data_gatherer.city_name} | Desc:{weather_data.description}, CurrT:{weather_data.current_temp}, FLT:{weather_data.feels_like_temp}, Range:{weather_data.temp_min} to {weather_data.temp_max}, Press:{weather_data.pressure}, Hum:{weather_data.humidity}, Wind:{weather_data.wind_speed}\n')

def db_log_weather_data(data_gatherer,weather_data):
    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_INSERT_INTO_LOG,(data_gatherer.city_name,weather_data.description,weather_data.current_temp,weather_data.feels_like_temp,weather_data.temp_min,weather_data.temp_max,weather_data.pressure,weather_data.humidity,weather_data.wind_speed,))

def db_log_error(error):
    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_INSERT_INTO_ERROR_LOG,(str(error),))

data_gatherer = DataGatherer('Tczew','metric',api_key)

while True:
    for i in range(5):
        try:
    
            data = data_gatherer.gather_data()
            weather_data = Weather(data)
        except ConnectionError as Argument:
            print(f'An error occured: {Argument}\n')
            db_log_error(Argument)
            time.sleep(6)
            continue
        break
    current_time = datetime.datetime.now()

    for i in range(5):   
        try:
            if current_time.minute == 00:
        
                data = data_gatherer.gather_data()
                weather_data = Weather(data)
                db_log_weather_data(data_gatherer,weather_data)
                console_log_weather_data()
            else:
                console_log_weather_data()
        except Exception as Argument:
            print(f'An error occured: {Argument}')
            db_log_error(Argument)
            time.sleep(6)
            continue
        break
    time.sleep(60)