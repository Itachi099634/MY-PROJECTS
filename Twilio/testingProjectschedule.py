from twilio.rest import Client
import datetime
import time
import schedule


account_sid = "AC736de64606ce201d8deadc6e53e3db70"
auth_token = "8127a96d6974928e1620e37742d9c74e"

client = Client(account_sid, auth_token)

numbers=[
    "whatsapp:+919643292600",
    "whatsapp:+918178886307"
]

def send_message(num):
   message = client.messages.create(
    body="Hello! This message is sent using Python and Twilio.",
    from_="whatsapp:+14155238886", 
    to=num

)
   def send_message(num):
    print("Message sent to", num)
   return message

def wait_seconds():
 if wait_seconds> 0:
    print(f"Waiting {wait_seconds} seconds before sending the message...")
    time.sleep(wait_seconds)


def target_time():
    target_time = datetime.datetime(2026, 3, 15, 5, 22)
    now = datetime.datetime.now()
    return target_time, now

target_time, now = target_time()

if now < target_time:
    delay = (target_time - now).total_seconds()
    print(f"Waiting {delay} seconds until {target_time}...")
    time.sleep(delay)
    
    for num in numbers:
     message = send_message(num)
     print("Message sent successfully!")
     print("Message SID:", message.sid)
else:
    print("Target time has already passed. Message not sent.")
    


    
