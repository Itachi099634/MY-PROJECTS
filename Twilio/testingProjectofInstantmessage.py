from twilio.rest import Client
import datetime
import time
import schedule

account_sid = "AC736de64606ce201d8deadc6e53e3db70"
auth_token = "8127a96d6974928e1620e37742d9c74e"

client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
        body="Hello! This message is sent using Python and Twilio.",
        from_="whatsapp:+14155238886",
        to="whatsapp:+918178886307"
    )
    print("Message sent successfully!")
    print("Message SID:", message.sid)

hour = 5
minute = 10

schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)