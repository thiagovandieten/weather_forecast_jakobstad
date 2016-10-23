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

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

main()
