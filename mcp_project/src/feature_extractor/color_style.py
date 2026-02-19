# src/feature_extractor/color_style.py
import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract(video_path: str, debug: bool = False) -> list:
    """
    Extracts dominant color palette from a video using KMeans clustering.

    Args:
        video_path (str): Path to video file
        debug (bool): Print extra details if True

    Returns:
        list of str: Dominant colors in HEX format
    """
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_count == 0 or not cap.isOpened():
        return ["No frames to analyze"]

    # Sample 5 evenly spaced frames
    sample_frames = [int(frame_count * i / 5) for i in range(5)]
    all_pixels = []

    for frame_index in sample_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (160, 90))  # downsize for speed
        pixels = frame.reshape(-1, 3)  # flatten to RGB list
        all_pixels.extend(pixels)

    cap.release()

    if not all_pixels:
        return ["Color extraction failed"]

    try:
        kmeans = KMeans(n_clusters=5, random_state=42, n_init="auto")
        kmeans.fit(np.array(all_pixels))
        colors = kmeans.cluster_centers_.astype(int)

        hex_colors = ["#%02x%02x%02x" % tuple(color) for color in colors]
        if debug:
            print("🎨 Dominant Colors:", hex_colors)
        return hex_colors

    except Exception as e:
        return [f"KMeans error: {str(e)}"]
