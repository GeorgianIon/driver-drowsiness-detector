from app.detector import detect_drowsiness

def test_detect_alert():
    result = detect_drowsiness("sample_images/alert1.jpg")
    assert result["status"] == "alert"
    assert result["eyes_detected"] >= 2

def test_detect_sleepy():
    result = detect_drowsiness("sample_images/sleepy1.jpg")
    assert result["status"] == "sleepy"
    assert result["eyes_detected"] < 2

def test_invalid_path():
    result = detect_drowsiness("sample_images/nu-exista.jpg")
    assert "error" in result
