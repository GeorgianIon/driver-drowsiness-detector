# driver-drowsiness-detector

Driver Drowsiness Detector – Python API Project

This project implements a simple proof-of-concept system to detect potential driver drowsiness from facial images. It uses OpenCV’s Haar cascade to identify the presence of eyes in the image and estimates the driver’s status as `alert` or `sleepy`.

---

## Features

- Detects presence of eyes in an image using Haar cascade  
- Classifies driver as `sleepy` or `alert` based on detection logic  
- Exposes a FastAPI endpoint `/predict` for image upload and prediction  
- Includes unit tests and API tests using `pytest`  
- Minimal, clean codebase suitable for learning or CV/demo use  

---

## How It Works

- Input: A facial image of the driver
- Step 1: Convert image to grayscale
- Step 2: Detect eyes using Haar cascade classifier
- Step 3: Classify as:
  - `alert` → if 2 or more eyes detected
  - `sleepy` → if fewer than 2 eyes detected
- Output: JSON response with status and number of detected eyes

---

##  Tech Stack

- Python 3.x
- OpenCV
- FastAPI
- Uvicorn
- Pytest

---
