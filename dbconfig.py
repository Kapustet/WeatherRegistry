dbconfig =  {'host':'127.0.0.1',
                'user':'',
                'password':'',
                'database':'',}

_SQL = """insert into log (city,description,currTemp,feelsLike,minTemp,maxTemp,pressure,humidity,windSpeed) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""