from fastapi import FastAPI, File, UploadFile
from app.detector import detect_drowsiness
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    # Salvăm fișierul uploadat temporar
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = detect_drowsiness(file_location)

    # Ștergem fișierul după analiză
    os.remove(file_location)

    return result
