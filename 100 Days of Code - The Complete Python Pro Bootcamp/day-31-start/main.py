import json
import random
import smtplib
import datetime as dt

MAIL_SUBJECT = 'Monday Motivation'

with open('quotes.txt', 'r') as quotes_file:
    all_quotes = quotes_file.readlines()

quote_of_the_day: str = random.choice(all_quotes)
quote, author =  [x.strip() for x in quote_of_the_day.split('-')]

with open('secrets.json', 'r') as secrets_file:
    secrets = json.load(secrets_file)

def send_email():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=secrets['email'], password=secrets['password'])
        connection.sendmail(from_addr=secrets['email'],
                            to_addrs=secrets['send_to'],
                            msg=f'subject: {MAIL_SUBJECT}\n\n'
                                f'{author} said: \n\n'
                                f'{quote}\n\n\n\n'
                                f'Don\'t worry, it\'s not spam and they didn\'t hack my account')

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 6:
    send_email()