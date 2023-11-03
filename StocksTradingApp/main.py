import os

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ["NEWS_API_KEY"]


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["bot_token"]
    bot_chat_id = os.environ["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)

    telegram_response = requests.get(send_text)

    return telegram_response.json()


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

different = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if different > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((different / float(yesterday_closing_price)) * 100)

if abs(diff_percentage) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}:{up_down}{diff_percentage}%\nHeadline:{article['title']}.\nBrief:{article['description']}" for
        article in three_articles]

    for article in formatted_articles:
        message = telegram_bot_send_text(article)
