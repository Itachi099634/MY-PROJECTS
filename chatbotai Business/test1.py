from flask import Flask, request, jsonify
import requests
import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx # type: ignore

app = Flask(__name__)



# 🔐 CONFIG
ACCESS_TOKEN = "YOUR_WHATSAPP_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
VERIFY_TOKEN = "my_verify_token"

openai.api_key = "YOUR_OPENAI_API_KEY"

# 📩 Send WhatsApp Message
def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }

    requests.post(url, headers=headers, json=data)

# 🧠 AI RESPONSE FUNCTION
def get_ai_reply(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional customer support assistant for a clothing business. Be polite, helpful, and business-focused."},
            {"role": "user", "content": user_message}
        ]
    )

    return response["choices"][0]["message"]["content"]

# 🔍 Verify Webhook
@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Verification failed"

# 📥 Receive Messages
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        from_number = message["from"]
        user_text = message["text"]["body"]

        print("User:", user_text)

        # 🤖 AI reply
        ai_reply = get_ai_reply(user_text)

        send_whatsapp_message(from_number, ai_reply)

    except Exception as e:
        print("Error:", e)

    return jsonify({"status": "ok"})

# ▶️ Run Server
if __name__ == "__main__":
    app.run(port=5000, debug=True)