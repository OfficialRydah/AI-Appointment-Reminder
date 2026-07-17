from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")


def make_call(client_name, phone_number):
    try:

        print(f"Calling {client_name}")
        print(f"Phone: {phone_number}")
        print("Using URL:")
        print("https://aversion-reissue-exodus.ngrok-free.dev/voice")

        call = client.calls.create(
            to=phone_number,
            from_=TWILIO_NUMBER,
            url="https://aversion-reissue-exodus.ngrok-free.dev/voice",
            method="GET"
        )

        print("Call SID:", call.sid)

    except TwilioRestException as e:
        print("Twilio Error:")
        print(e)