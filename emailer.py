import circus_email
import schedule
import weather

def main():
    emails = circus_email.get_emails()
    # print(emails)

    schedule_today = schedule.get_schedule()
    # print(schedule)

    forecast = weather.get_weather_forecast()

    circus_email.send_emails(emails, schedule_today, forecast)

main()
