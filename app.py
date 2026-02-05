from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
import yt_dlp, uuid, os

app = Flask(__name__)

def download_audio(song):
    name = f"{uuid.uuid4()}.mp3"
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': name,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{song}"])
    return name

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    text = request.values.get("Body", "")
    resp = MessagingResponse()
    msg = resp.message()

    if len(text) > 3:
        audio = download_audio(text)
        url = f"https://YOUR-APP-URL.onrender.com/{audio}"
        msg.media(url)
        msg.body("🎧 Tomar gan ready!")
    else:
        msg.body("🎶 Ganer naam ba lyrics lekho")

    return str(resp)

@app.route("/<filename>")
def audio(filename):
    return send_from_directory(".", filename)
