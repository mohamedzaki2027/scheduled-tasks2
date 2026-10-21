import os
from twilio.rest import Client


class TwilioManager():

    ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
    RECEIVER_MOBILE = os.environ.get('T_RECEIVER_MOBILE')
    SENDER_MOBILE = os.environ.get('T_SENDER_MOBILE')

    def __init__(self) -> None:
        pass

    def send_message(self, msg: str = "Get Ready. It will Rain ☔"):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

        message = client.messages.create(
            to=f"whatsapp:{self.RECEIVER_MOBILE}",
            from_=f"whatsapp:{self.SENDER_MOBILE}",
            content_sid="HX8dc9eea84231541b091557c47cc2a342",
        )

        print(message.sid, message.status)
