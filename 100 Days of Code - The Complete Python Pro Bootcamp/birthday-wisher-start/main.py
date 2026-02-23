##################### Extra Hard Starting Project ######################
import datetime
import random
import smtplib
import json
import pandas as pd

MAIL_SUBJECT='HAPPY BIRTHDAY'

# 1. Update the birthdays.csv
with open('birthdays.csv', 'r') as file:
    birthdays = pd.read_csv(file).to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
birthday_today = [x for x in birthdays
                  if x['month'] == today.month
                  and x['day'] == today.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(birthday_today)>0:
    rand_option = random.randint(1,3)

    with open(f'letter_templates/letter_{rand_option}.txt') as letter:
        template = letter.read()


# 4. Send the letter generated in step 3 to that person's email address.
with open('secrets.json', 'r') as secrets_file:
    secrets = json.load(secrets_file)

def send_email(name):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=secrets['email'], password=secrets['password'])
        connection.sendmail(from_addr=secrets['email'],
                            to_addrs=secrets['send_to'],
                            msg=f'subject: {MAIL_SUBJECT}\n\n'
                                f'{template.replace("[NAME]", name)}')

for bd in birthday_today:
    send_email(bd['name'])




