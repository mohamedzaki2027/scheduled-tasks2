import os
from typing import cast
import http.client
import json


class InfobipManager():

    INFOBIP_SMS_ENDPOINT_URL = cast(
        str, os.environ.get('INFOBIP_SMS_ENDPOINT_URL'))
    INFOBIP_API_KEY = os.environ.get('INFOBIP_API_KEY')
    RECEIVER_MOBILE = os.environ.get('I_RECEIVER_MOBILE')
    SENDER_MOBILE = os.environ.get('I_SENDER_MOBILE')

    def __init__(self) -> None:
        pass

    def send_message(self, msg: str = "Get Ready. It will Rain ☔"):
        conn = http.client.HTTPSConnection(self.INFOBIP_SMS_ENDPOINT_URL)
        payload = json.dumps({
            "messages": [
                {
                    "destinations": [
                        {
                            "to": self.RECEIVER_MOBILE
                        }
                    ],
                    "sender": self.SENDER_MOBILE,
                    "content": {
                        "text": msg
                    }
                }
            ]
        })
        headers = {
            'Authorization': f'App {self.INFOBIP_API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        conn.request("POST", "/sms/3/messages", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
