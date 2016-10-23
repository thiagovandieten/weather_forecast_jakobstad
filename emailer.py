import requests
import smtplib

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

def send_emails(emails, schedule, forecast):
    try:
        # Get the emailer's user & pass
        # account_file = open('mailaccount.txt', 'r')
        # (from_email, password) = account_file.readline().split(',')
        # account_file.close()

        #Changed to using input from the user itself
        from_email = input('Please login into the mail server with your email: ')
        from_email = from_email.strip()
        password = input('And your password: ').strip()

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', '587')

        #Start TLS encryption
        server.starttls()
        server.login(from_email, password)
        server.set_debuglevel(1)

        for address, name in emails.items():
            message = 'Subject: Welcome to the circus!\n'
            message += 'Hi ' + name + '!\n\n'
            message += forecast + '\n\n'
            message += schedule + '\n\n'
            message += 'Hope to see you there!'
            server.sendmail(from_email, address, message)

        server.quit()

    except Exception as err:
        print(err)

def main():
    emails = get_emails()
    # print(emails)

    schedule = get_schedule()
    # print(schedule)

    forecast = get_weather_forecast()

    send_emails(emails, schedule, forecast)

main()
