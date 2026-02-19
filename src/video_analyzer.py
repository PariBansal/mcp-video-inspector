from src.feature_extractor import (
    ai_advanced_effects,
    color_style,
    transitions_effects,
    # audio_analysis,  # Audio analysis disabled
    typography_text,
    camera_work,
    mood_tone
)
from src.llm_summary import generate_summary 

def analyze_video(video_path: str, audio_path: str) -> dict:
    """
    Analyze a video for technical and creative editing features (audio skipped).

    Args:
        video_path (str): Path to the .mp4 video file.
        audio_path (str): Path to the .wav audio file (ignored).

    Returns:
        dict: A dictionary of extracted features and LLM summary (optional).
    """
    print("🧠 Starting video feature extraction...\n")
    features = {}

    extractors = {
        "Color & Visual Style": lambda: color_style.extract(video_path),
        "Transitions & Effects": lambda: transitions_effects.extract(video_path),
        "Audio Design": lambda: {
            "status": "skipped",
            "note": "Audio analysis intentionally disabled for this run."
        },
        "Typography & Text": lambda: typography_text.extract(video_path),
        "Camera Work": lambda: camera_work.extract(video_path),
        "Mood & Tone": lambda: mood_tone.extract(video_path),
        "AI/Advanced Features": lambda: ai_advanced_effects.extract(video_path),
    }

    for name, extractor in extractors.items():
        try:
            print(f"🔍 Extracting: {name}...")
            features[name] = extractor()
        except Exception as e:
            print(f"⚠️ Failed to extract {name}: {e}")
            features[name] = {"error": str(e)}

    print("\n🧠 Generating creative LLM summary...")
    features["LLM Summary"] = (
        "🧠 LLM Summary is disabled.\n"
        "📌 Use Cursor AI or manually review the extracted features above "
        "to interpret editing style, mood, and tone."
    )

    print("✅ Feature extraction complete.")
    return features
