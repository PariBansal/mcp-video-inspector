# src/feature_extractor/ai_advanced_features.py

import cv2
import numpy as np

def extract(video_path: str) -> list:
    """
    Analyze a middle frame to detect signs of AI-enhanced visuals.
    Heuristic: High resolution or abnormally sharp images may indicate AI upscaling/sharpening.
    """
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames == 0:
        cap.release()
        return ["Invalid video"]

    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames // 2)
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        return ["Frame extraction failed"]

    height, width = frame.shape[:2]
    sharpness = cv2.Laplacian(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()

    # Heuristic thresholds
    tags = []
    if height >= 1440 or width >= 2560:
        tags.append("Upscaled to 2K+")
    elif height >= 1080:
        tags.append("Full HD Resolution")

    if sharpness > 300:
        tags.append("Sharpened (possible AI enhancement)")
    elif sharpness < 50:
        tags.append("Soft focus or natural image")

    return tags if tags else ["Standard Quality"]
