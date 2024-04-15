import requests
import smtplib

LAT = 41.878113
LONG = -87.629799
API = "apikeyhere"
EMAIL = "myemail@gmail.com"
PW = "myveryunsecurepassword:P"

resp = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&cnt=4&appid={API}').json()
forecasts = resp['list']

will_rain = False
for fc in forecasts:
    id = fc['weather'][0]["id"]
    desc = fc['weather'][0]['description']
    if id < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PW)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Weather Alert!\n\nIt's going to rain today. Bring an umbrella!"
        )
