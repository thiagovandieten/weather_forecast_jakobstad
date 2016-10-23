import requests

emails = {}

def get_emails():

    try:
        email_file = open('emails.txt', 'r') #CSV, starting with email.

        for line in email_file:
            line = line.strip()
            (email, name) = line.split(',')
            emails[email] = name

        email_file.close()
        return emails

    except FileNotFoundError as err:
        print(err)

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
        schedule_file.close()
        return schedule

    except FileNotFoundError as err:
        print(err)

def get_weather_forecast():
    #City ID: 656130
    #API key: 9f57233f8f1a7130f3952bc02a84139e
    url = 'http://api.openweathermap.org/data/2.5/weather?id=656130&units=metric&APPID=9f57233f8f1a7130f3952bc02a84139e'
    r = requests.get(url)
    weather_json = r.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'The circus of Jakobstad\'s forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += 'C\u00b0 and a low of ' + str(int(temp_min)) + 'C\u00b0'

    print(forecast)

def main():
    # emails = get_emails()
    # print(emails)
    #
    # schedule = get_schedule()
    # print(schedule)

    get_weather_forecast()

main()
