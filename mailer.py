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
