import smtplib
import datetime as dt
import random
    
with open("quotes.txt") as quotes:
    content = quotes.read().splitlines()

quote = random.choice(content)

now = dt.datetime.now()
# 0 monday, 1 tues, 2 wed
weekday = now.weekday()

if weekday == 2:
    my_email = "myemail@gmail.com"
    pw = "passwordhere"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="someoneelse@gmail.com", 
            msg=f"Subject: Motivational Quote\n\n{quote}")
