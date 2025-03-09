from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, ImageMessage, TextSendMessage
import requests
import datetime
import random
from face_detector import check_face
from time_checker import generate_response

# ตั้งค่า LINE Bot
LINE_ACCESS_TOKEN = "3U/MMEJshhpTHNS10H5aC6A9kRnNUu/M8iBBidVmcdF6+FHiPyC1PNMy/Seg3/sf2vaYc/mgYGNLa9j3Pn1/nz35lOOMQhFyFoctIZ2PBTg5E2xASnIwkxEtME7tN+vM5GNlKPeku2MQzSbjZybuTAdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "025257faa310a7579cfa21ceb9480c98"
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print(body)  # ตรวจสอบข้อมูลที่ได้รับ
    if "events" in body and len(body["events"]) > 0:
        handler.handle(body["events"][0])
    return "OK"

@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    # ดึง URL ของรูปภาพที่ส่งมา
    image_id = event.message.id
    image_url = f"https://api-data.line.me/v2/bot/message/{image_id}/content"

    # ดาวน์โหลดรูปภาพ
    headers = {"Authorization": f"Bearer {LINE_ACCESS_TOKEN}"}
    response = requests.get(image_url, headers=headers, stream=True)
    
    with open("temp.jpg", "wb") as f:
        for chunk in response.iter_content():
            f.write(chunk)

    # ตรวจจับใบหน้า
    if check_face("temp.jpg"):
        user_id = event.source.user_id
        current_time = datetime.datetime.now().strftime("%H:%M")
        response_text = generate_response(user_id, current_time)
    else:
        response_text = "ไม่พบใบหน้าในรูป กรุณาถ่ายใหม่!"

    # ตอบกลับไปที่ LINE
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response_text))

if __name__ == "__main__":
    app.run()
