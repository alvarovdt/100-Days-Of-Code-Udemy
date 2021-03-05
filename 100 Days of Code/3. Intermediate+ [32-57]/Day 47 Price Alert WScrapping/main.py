import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.es/Apple-MWP22TY-A-AirPods-Pro/dp/B07ZPNLGDP"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("\xa0")[0].replace(",", ".")
price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 300

YOUR_EMAIL = ""
YOUR_PASSWORD = ""
YOUR_SMTP_ADDRESS = "smtp.gmail.com"
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )