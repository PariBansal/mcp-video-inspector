from flask import Blueprint, request, jsonify
import os
import uuid

from src.video_downloader import download_video
from src.video_analyzer import analyze_video
from src.feature_extractor.extract_audio import extract_audio_with_ffmpeg
from src.llm_summary import summarize_features

bp = Blueprint("analyze_route", __name__, url_prefix="/analyze")

@bp.route("/video", methods=["POST"])
def analyze_from_youtube():
    data = request.get_json()
    url = data.get("youtube_url")
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Step 1: Prepare temp folder and paths
        temp_folder = "temp_videos"
        os.makedirs(temp_folder, exist_ok=True)
        video_filename = str(uuid.uuid4()) + ".mp4"
        audio_filename = video_filename.replace(".mp4", ".wav")

        video_path = os.path.join(temp_folder, video_filename)
        audio_path = os.path.join(temp_folder, audio_filename)

        # Step 2: Download video
        print("📥 Downloading video...")
        download_video(url, output_path=video_path)
        print(f"✅ Video saved at {video_path}")

        # Step 3: Extract audio if not already there
        if not os.path.exists(audio_path):
            print("🎧 Extracting audio...")
            extract_audio_with_ffmpeg(video_path, audio_path)
        else:
            print("✅ Audio already exists, skipping extraction.")

        # Step 4: Analyze
        print("🧠 Analyzing video and audio...")
        features = analyze_video(video_path, audio_path)

        # Step 5: Generate summary
        print("📝 Generating LLM summary...")
        summary = summarize_features(features)

        # Optional Cleanup
        # os.remove(video_path)
        # os.remove(audio_path)

        return jsonify({
            "features": features,
            "summary": summary
        }), 200

    except Exception as e:
        print("❌ Error during analysis:", str(e))
        return jsonify({"error": str(e)}), 500
