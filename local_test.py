# -*- coding: utf-8 -*-
"""
Created on Mon May  5 14:21:16 2025

@author: Georgian
"""

from app.detector import detect_drowsiness

result = detect_drowsiness("sample_images/alert_image1.png")
print(result)