import os

import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=nutritionix_params)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
today_hour = datetime.now().strftime("%H:%M:%S")

sheet_endpoint = os.environ["sheet_endpoint"]

bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(response.text)
