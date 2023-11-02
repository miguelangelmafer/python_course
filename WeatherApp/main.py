import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""

account_sid = ""
auth_token = ""

weather_params = {
    "lat": 45.464203,
    "lon": 9.189982,
    "appid": API_KEY,
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+",
        to="+"
    )
    print(message.status)
