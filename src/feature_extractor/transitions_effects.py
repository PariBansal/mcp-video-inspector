# src/feature_extractor/transitions_effects.py
import cv2
import numpy as np

def extract(video_path: str, debug: bool = False) -> list:
    """
    Detects editing transition style in a video using optical frame differencing.
    Also attempts to guess the effect style based on frame change magnitude.

    Args:
        video_path (str): Path to the video file.
        debug (bool): Whether to enable debug logging.

    Returns:
        list: Detected style, number of transitions, effect type, and frame count.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return ["Error: Could not open video"]

    prev_gray = None
    transitions = 0
    frames_checked = 0

    FRAME_INTERVAL = 5
    DIFF_THRESHOLD = 50
    EFFECT_THRESHOLD = 100  # If the diff is too sharp, may indicate heavy/special effect
    TRANSITION_RATIO_THRESHOLD = 0.3

    special_effects_used = False
    effect_names = []

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % FRAME_INTERVAL == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if prev_gray is not None:
                diff = cv2.absdiff(prev_gray, gray)
                mean_diff = np.mean(diff)

                if mean_diff > DIFF_THRESHOLD:
                    transitions += 1

                    # Detect potential effect names based on strength
                    if mean_diff > EFFECT_THRESHOLD:
                        special_effects_used = True
                        effect_names.append("Flash Cut / External Effect")

                    elif 70 < mean_diff <= EFFECT_THRESHOLD:
                        effect_names.append("Luma Fade / Wipe")

                    elif 50 < mean_diff <= 70:
                        effect_names.append("Cross Dissolve / Simple Cut")

                    if debug:
                        print(f"🎬 Transition @ frame {frame_count} | Δ={mean_diff:.2f}")

            prev_gray = gray
            frames_checked += 1

        if debug and frame_count % 50 == 0:
            print(f"📽️ Processed {frame_count} frames...")

        frame_count += 1

    cap.release()

    if frames_checked == 0:
        return ["Transition Detection: Not enough data"]

    transition_ratio = transitions / frames_checked
    style = "Fast Cuts" if transition_ratio > TRANSITION_RATIO_THRESHOLD else "Slow/Gradual Transitions"

    if not effect_names:
        effect_names.append("No obvious named effects detected")

    summary = [
        style,
        f"Detected Transitions: {transitions}",
        f"Frames Analyzed: {frames_checked}",
        f"Named Effects Detected: {list(set(effect_names))}"
    ]

    if special_effects_used:
        summary.append("⚡ Special or External Effects likely used")

    return summary
