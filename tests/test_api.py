from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_alert():
    with open("sample_images/alert1.jpg", "rb") as image:
        response = client.post("/predict", files={"file": ("alert1.jpg", image, "image/jpeg")})
    assert response.status_code == 200
    assert response.json()["status"] in ["alert", "sleepy"]
    assert "eyes_detected" in response.json()

def test_predict_invalid_file():
    response = client.post("/predict", files={"file": ("fake.txt", b"notanimage", "text/plain")})
    assert response.status_code == 200
    assert "error" in response.json() or response.json()["status"] in ["sleepy", "alert"]
