from flask import Flask, request
import os
from groq import Groq
import twilio.twiml.messaging_response

app = Flask(__name__)

SYSTEM_PROMPT = "You are a helpful assistant."

MODEL = "llama-3.3-70b-versatile"
MAX_TOKENS = 1024

conversation = []

def get_reply(user_input):
    global client, conversation
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation
    )

    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})

    return reply

def get_api_key():
    return os.environ.get("GROQ_API_KEY")

def chat():
    global client, conversation
    print(get_api_key())
    print("API KEY:", get_api_key())
    client = Groq(api_key=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)
    conversation = []

    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break

        if user_input.lower() == "clear":
            conversation.clear()
            print("Conversation history cleared.")
            continue

        conversation.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation
        )

        assistant_text = response.choices[0].message.content
        print("Assistant:", assistant_text)
        
        conversation.append({"role": "assistant", "content": assistant_text})

@app.route("/message", methods=["POST"])
def reply():
    incoming_msg = request.form.get("Body")
    reply_text = get_reply(incoming_msg)
    resp = twilio.twiml.messaging_response.MessagingResponse()
    resp.message(reply_text)

    return str(resp)

if __name__ == "__main__":
    client = Groq(api_key=get_api_key())
    app.run(port=5000)
    app.run(debug=True)