import pandas
import smtplib
import datetime as dt
import random

birthday_csv = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_csv.to_dict(orient="records")


for birthdays in birthday_dict:
    if birthdays["month"] == dt.datetime.now().month and birthdays["day"] == dt.datetime.now().day:
        letter_templates_rand = random.randint(1, 3)

        with open(f"./letter_templates/letter_{letter_templates_rand}.txt") as file:
            text = file.read()
            text = text.replace("[NAME]", birthdays["name"])
            my_email = MY_EMAIL
            password = MY_PASS
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=birthdays["email"],
                                    msg=f"Subject:Happy Birthday!! \n\n{text}"
                                    )






