emails = {}
try:
    email_file = open('emails.txt', 'r')

    for line in email_file:
        line = line.strip()
        (email, name) = line.split(',')
        emails[email] = name

    email_file.close()
    print(emails)

except FileNotFoundError as err:
    print(err)
