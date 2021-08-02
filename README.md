# Weather Data Gathering Project.

Making calls to [Open Weather API](https://openweathermap.org) in order to obtain current weather data. Logging them to the MariaDB database every full hour(e.g. 7:00 o'clock) and printing to the console every minute.

## Requirements:

* [Python 3.x](https://www.python.org/downloads/) and some depencencies
	* [virtualenv](https://pypi.org/project/virtualenv/) 
	* requirements.txt (included in project files)
* [MariaDB 10.6](https://mariadb.org/download/)

In order for the project to work, two Python files require your attention: apiKey, dbconfig. Both of them have a base template, it just needs to be filled with your unique api key(obtained [here](https://openweathermap.org/api) and database configuration accordingly.
	

### Using Virtualenv to create an environment dedicated to the project.

1. Create an environment
```
python -m venv environment_name
```
2. Activate the environment
```
environment_name\Scripts\activate.bat
```
3. Download the required dependencies
```
pip install -r requirements.txt
```
## Creating a database
Refer to DatabaseCreationInstructions.txt.



## Problems and possible solutions
* [mysql is not recognised as an internal or external command,operable program or batch](https://stackoverflow.com/questions/5920136/mysql-is-not-recognised-as-an-internal-or-external-command-operable-program-or-b)
