dbconfig =  {'host':'127.0.0.1',
                'user':'WeatherRegistry',
                'password':'weatherregistrypasswd',
                'database':'WeatherRegistryLogsDB',}

_INSERT_INTO_LOG = """insert into log (city,description,currTemp,feelsLike,minTemp,maxTemp,pressure,humidity,windSpeed) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

_INSERT_INTO_ERROR_LOG = """insert into error_log (description) values (%s)"""
