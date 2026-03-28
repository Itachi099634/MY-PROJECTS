from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def chatbot_reply(message):
    message = message.lower()

    if "hello" in message:
        return "Hi! How can I help you?"
    elif "Who are you?" in message:
        return "I am a simple chatbot created for testing Twilio Conversations Created by Mani."
    elif "What can you do?" in message:
        return "I can respond to basic greetings and questions. Try asking me something!"
    elif "Tell me some knowledgeable information" in message:
        return "Well Do you know that Our solar system is a vast and 4.6 billion years old"
    elif "That's actually interesting" in message:
        return "I'm glad you found it interesting! If you have any more questions or want to know about something else, just ask!"
    elif "Can you also tell me a joke?" in message:
        return "Sure! Why don't scientists trust atoms? Because they make up everything!"
    elif "Well this was a great conversation with you" in message:
        return "Thank you! I'm glad you enjoyed our conversation. If you have any more questions or just want to chat, feel free to reach out anytime!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
     
@app.route("/message", methods=["POST"])
def reply():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    msg = response.message()

    reply_text = chatbot_reply(incoming_msg)
    msg.body(reply_text)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)