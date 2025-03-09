from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, ImageMessage, TextSendMessage
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    return "Webhook Active!"

# รองรับการรันบน Vercel
def lambda_handler(event, context):
    return app(event, context)
