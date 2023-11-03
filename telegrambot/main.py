import os

import requests


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["bot_token"]
    bot_chat_id = os.environ["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)

    response2 = requests.get(send_text)

    return response2.json()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ["OWM_API_KEY"]

weather_params = {
    "lat": 45.464203,
    "lon": 9.189982,
    "appid": OWM_API_KEY,
    "units": "metric",
    "lang": "es"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = telegram_bot_send_text("Va a llover")
    if message["ok"]:
        print("Mensaje enviado")
    else:
        print(message)
