# src/feature_extractor/camera_work.py

import cv2
import numpy as np

def extract(video_path: str, debug: bool = False) -> list:
    cap = cv2.VideoCapture(video_path)
    motions = []

    prev_gray = None
    frame_count = 0
    FRAME_INTERVAL = 5  # Process every 5th frame

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % FRAME_INTERVAL == 0:
            try:
                frame = cv2.resize(frame, (320, 180))  # Speed up
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if prev_gray is not None:
                    flow = cv2.calcOpticalFlowFarneback(
                        prev_gray, gray,
                        None, 0.5, 3, 15, 3, 5, 1.2, 0
                    )
                    mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
                    motions.append(np.mean(mag))

                prev_gray = gray

                if debug and frame_count % 50 == 0:
                    print(f"📽️ Processed {frame_count} frames...")

            except Exception as e:
                if debug:
                    print(f"⚠️ Frame {frame_count} skipped due to error: {e}")
                continue

        frame_count += 1

    cap.release()

    if not motions:
        return ["Camera motion: Not enough data"]

    avg_motion = np.mean(motions)

    if avg_motion < 0.5:
        motion_type = "Static or Tripod"
    elif avg_motion < 2.0:
        motion_type = "Moderate Motion (e.g., pans, slides, Steadicam)"
    else:
        motion_type = "High Motion (e.g., handheld, action shots)"

    return [motion_type, f"Avg Motion Intensity: {avg_motion:.2f}", f"Frames Processed: {frame_count}"]
