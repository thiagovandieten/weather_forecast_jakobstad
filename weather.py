import requests

def get_weather_forecast():
    #Depends on the requests module
    url = 'http://api.openweathermap.org/data/2.5/weather?id=656130&units=metric&APPID=9f57233f8f1a7130f3952bc02a84139e'
    r = requests.get(url)
    weather_json = r.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    city = weather_json['name']

    forecast = 'The circus of ' + city + '\'s forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' celsius and a low of ' + str(int(temp_min)) + ' celsius'

    return forecast
