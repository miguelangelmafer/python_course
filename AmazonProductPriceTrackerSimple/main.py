import os

import requests
from bs4 import BeautifulSoup


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["bot_token"]
    bot_chat_id = os.environ["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)

    response2 = requests.get(send_text)

    return response2.json()


URL = ("https://www.amazon.es/Nothing-Ear-Auriculares-inal%C3%A1mbricos-Personalizado/dp/B0C5J9SL3Y/ref=sr_1_4?crid"
       "=31PFXV81XATB6&keywords=nothing&qid=1700217127&s=electronics&sprefix=nothing%2Celectronics%2C472&sr=1-4&th=1")
HEADERS = {
    "Accept-Language": "es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.content, 'html.parser')
product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().split("-")[0].strip()
whole_price = soup.find(name="span", class_="a-price-whole").getText().split(",")[0]
decimal_price = soup.find(name="span", class_="a-price-fraction").getText()
full_price_amz = float(whole_price + "." + decimal_price)

MIN_PRICE = 110

if full_price_amz < MIN_PRICE:
    telegram_bot_send_text(f"‼️El artículo {product_name} ha bajado de precio. Ahora cuesta: {full_price_amz}€")
