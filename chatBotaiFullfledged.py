import pywhatkit 
import datetime

number = "+919643292600"

def chatbot_reply(message):
    message = message.lower()
    
    if "hello" in message:
        return "Hello Sir/Madam, How can I help you?"
    elif "time" in message:
        now = datetime.datetime.now()
        return "Current time is " + str(now.strftime("%H:%M"))
    elif "name" in message:
        return "I am Mani's Chatbot Ai How can i assist you today?"
    elif "send message" in message:
        return "Sorry Didnt understand that. Can you please retype that?"
    else: 
        return "Hello Sir/Madam, How can I help you?"

user = input("You:")

reply = chatbot_reply(user)

Date=13.06
hour= 5
minute= 30

print("Chatbot: " + reply)

pywhatkit.sendwhatmsg(number, reply, hour, minute)

print("message was sent successfully.")
    
