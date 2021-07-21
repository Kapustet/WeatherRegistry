import datetime
import time
import requests
from apiKey import apiKey


cityName = 'Tczew'
units = 'metric'
fullAddress = f'http://api.openweathermap.org/data/2.5/weather?q={cityName}&units={units}&appid={apiKey}'


while True:
    response = requests.get(fullAddress)
    data = response.json()
    print(type(data))
    currentTime = datetime.datetime.now()

    description = data['weather'][0]['description']
    currentTemp = data['main']['temp']
    feelsLikeTemp = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    windSpeed = data['wind']['speed'] 

    print(f'{currentTime} -> H:{currentTime.hour}|M:{currentTime.minute} ')

    if currentTime.minute == 0:
        print('Whole Hour:{:d}:{:02d}\n'.format(currentTime.hour, currentTime.minute))
        with open('WeatherLog.txt','a') as f:
            f.write(f'WHOLE HOUR: {currentTime}, City:{cityName}|| Description:{description}, CurrentTemperature:{currentTemp}, FeelsLikeTemperature:{feelsLikeTemp}, Ranging between:{temp_min} to {temp_max}, Pressure:{pressure}, Humidity:{humidity}, WindSpeed:{windSpeed}\n')
    else:
        print('{:d}:{:02d}\n'.format(currentTime.hour, currentTime.minute))

    time.sleep(60)