import datetime as dt
import smtplib
import random
import pandas

EMAIL = "myemail@gmail.com"
PW = "myunsecurepassword :P"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letters)

now = dt.datetime.now()
today = (now.month, now.day)


birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for index, row in birthdays.iterrows()}


if today in birthdays_dict:
    name = birthdays_dict[today].get('name')

    with open(f"./letter_templates/{letter}") as ltr:
        content = ltr.read()
        updated_content = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PW)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthdays_dict[today].get('email'),
            msg=f"Subject: Happy Birthday!\n\n{updated_content}"
        )
