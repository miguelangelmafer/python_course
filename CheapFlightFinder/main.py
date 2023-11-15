import os
from datetime import datetime, timedelta

import requests

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "ALC"


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["bot_token"]
    bot_chat_id = os.environ["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)

    response2 = requests.get(send_text)

    return response2.json()


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
one_month_from_today = datetime.now() + timedelta(days=30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price is not None and flight.price < int(destination["lowestPrice"]):
        telegram_bot_send_text(
            f"Low price alert! Only {flight.price}€ to fly from {flight.origin_city}-{flight.origin_airport} to "
            f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
