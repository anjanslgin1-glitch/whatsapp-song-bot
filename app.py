from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running OK"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming = request.values.get("Body", "")
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f"Tumi likhecho: {incoming}")
    return str(resp)

app.run(host="0.0.0.0", port=3000)
