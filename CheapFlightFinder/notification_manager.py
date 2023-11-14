import os

import requests


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["bot_token"]
    bot_chat_id = os.environ["bot_chat_id"]
    send_text = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id
                 + '&parse_mode=Markdown&text=' + bot_message)

    response2 = requests.get(send_text)

    return response2.json()
