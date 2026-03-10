import pywhatkit
import time

print("WhatsApp Reminder Chatbot")

number = input("Enter phone number: ")
message = input("Enter message: ")

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

print("Message scheduled...")

pywhatkit.sendwhatmsg(number, message, hour, minute)

print("YOGA CLASS WITHIN 30 MINUTES.")