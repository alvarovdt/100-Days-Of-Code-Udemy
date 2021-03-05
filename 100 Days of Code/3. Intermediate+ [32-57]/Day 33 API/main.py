import requests
from datetime import datetime
import smtplib
import time

# 1XX: HOld On
# 2XX: Here you go
# 3XX: Go Away
# 4XX: YOu screwed up
# 5XX: server error


parameters = {
    "lat": 41.385063,
    "lng": 2.173404,
    "formatted": 0
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_longitude)
    if parameters["lat"] - 5 <= iss_latitude <= parameters["lat"] + 5 and parameters["lng"] - 5 <= iss_latitude <= \
            parameters["lng"] + 5:
        return True


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T").split(":")[0])
    sunset = int(data["results"]["sunset"].split("T").split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True



while True:

    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = MY_EMAIL
        password = MY_PASSWORD
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky"
                                )
# if parameters["lat"]
# print(sunrise.split("T")[1].split(":")[0])
# print(sunset.split("T")[1].split(":")[0])
#
# time_now = datetime.now()
# #time_now = datetime.now()
# print(time_now)
