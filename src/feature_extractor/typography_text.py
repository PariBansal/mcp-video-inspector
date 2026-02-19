# src/feature_extractor/typography_text.py
import cv2
import pytesseract
import os

# Correct path to tesseract.exe (NOT the installer)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(video_path: str) -> list:
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    sample_frames = [int(frame_count * i / 5) for i in range(5)]  # sample 5 frames
    detected_text = set()

    for frame_index in sample_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Optional preprocessing for better OCR
        gray = cv2.medianBlur(gray, 3)

        # OCR
        text = pytesseract.image_to_string(gray)
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        detected_text.update(lines)

    cap.release()

    if not detected_text:
        return ["No text detected"]

    return list(detected_text)
