import Pywhatkit

print("Simple WhatsApp Chatbot")

name = input("Batko: ")
number = input("919643292600: ")
message = input("Enter the message you want to send: ")

print("Sending message...")

pywhatkit.sendwhatmsg_instantly(number, message)

print("Message sent successfully!")