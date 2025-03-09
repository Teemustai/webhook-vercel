import random

def generate_response(user_id, current_time):
    """ สุ่มข้อความตอบกลับตามช่วงเวลา """
    hour, minute = map(int, current_time.split(":"))

    if hour < 8:
        message = "มาตั้งแต่ไก่โห่เลยนะ!"
    elif hour == 8 and minute <= 30:
        message = "แหม่ ตรงเวลาเชียวนะ"
    elif hour < 9:
        message = "สายไปหน่อยนะวันนี้!"
    else:
        message = "มาช้าจังเลย! อย่าทำบ่อยล่ะ"

    return f"@{user_id} เข้างานเวลา {current_time} | {message}"
