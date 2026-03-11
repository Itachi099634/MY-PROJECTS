import pywhatkit 
import datetime
number =+919643292600

def chatbot_reply(message):
    message = message.lower()
    if "hello" in message:
        return "Hello Sir/Madam, How can I help you?"
    elif "time" in message:
        now = datetime.datetime.now()
        return "Current time is " + str(now.strftime("%H:%M"))
    elif "name" in message:
        return "I am Mani's Chatbot Ai How can i assist you today?"
    else:
        return"Sorry Didnt understand that. Can you please retype that?"
    if "send message to mani" in message:
        
        return "Sure I will send the message to Mani right away that you want to send to him."
    reply = chatbot_reply(user_message)
    print("Chatbot: " + reply)
    hour= 19
    minute = 45
    pywhatkit.sendwhatmsg(number, reply, hour, minute)
   
    print("message was sent successfully.")
    
