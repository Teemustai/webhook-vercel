import cv2

def check_face(image_path):
    """ ตรวจจับใบหน้าในภาพ """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    return len(faces) > 0  # ถ้ามีใบหน้าให้คืนค่า True
