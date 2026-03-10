import pywhatkit

print("Simple WhatsApp Chatbot")

name = input("Enter your name: ")
number = input("Enter the phone number (with country code): ")
message = input("Enter the message you want to send: ")

print("Sending message...")

pywhatkit.sendwhatmsg_instantly(number, message)

print("Message sent successfully!")

