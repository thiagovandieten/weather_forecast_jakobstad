import mailer
import schedule
import weather

def main():
    emails = mailer.get_emails()
    # print(emails)

    schedule_today = schedule.get_schedule()
    # print(schedule)

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule_today, forecast)

main()
