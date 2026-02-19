# src/feature_extractor/mood_tone.py
import cv2
import numpy as np

def extract(video_path: str) -> list:
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_count < 3:
        return ["Unknown Mood"]

    # Sample 3 frames: start, middle, end
    sample_indices = [0, frame_count // 2, frame_count - 1]
    brightness_values = []

    for idx in sample_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.resize(frame, (160, 90))  # Reduce size for speed
        avg_color = np.mean(frame.reshape(-1, 3), axis=0)
        brightness = np.mean(avg_color)
        brightness_values.append(brightness)

    cap.release()

    if not brightness_values:
        return ["Mood: Unknown"]

    avg_brightness = np.mean(brightness_values)

    if avg_brightness < 60:
        mood = "Dark/Moody"
    elif avg_brightness < 150:
        mood = "Neutral"
    else:
        mood = "Bright/Uplifting"

    return [f"Mood: {mood}", f"Avg Brightness: {round(avg_brightness, 2)}"]
