import cv2
import os

def detect_drowsiness(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Could not load image"}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cascade_path = os.path.join(os.path.dirname(__file__), "haarcascade_eye.xml")
    eye_cascade = cv2.CascadeClassifier(cascade_path)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(eyes) >= 2:
        return {"status": "alert", "eyes_detected": len(eyes)}
    else:
        return {"status": "sleepy", "eyes_detected": len(eyes)}
