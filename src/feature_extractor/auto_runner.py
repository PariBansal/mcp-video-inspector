from src.video_downloader import download_video
from src.video_analyzer import analyze_video

def summarize_youtube_video(url: str):
    print(f"🎥 Processing video from: {url}")
    
    try:
        # Step 1: Download video
        video_path = download_video(url, "downloads/test_video.mp4")
        print("✅ Video downloaded.")

        # Step 2: Analyze
        features = analyze_video(video_path, audio_path=video_path.replace(".mp4", ".wav"))
        print("✅ Features extracted.\n")

        # Step 3: Print in readable format
        for key, value in features.items():
            print(f"\n🔹 {key}:")
            if isinstance(value, dict):
                for k, v in value.items():
                    print(f"   • {k}: {v}")
            elif isinstance(value, list):
                for item in value:
                    print(f"   • {item}")
            else:
                print(f"   • {value}")

        print("\n🧠 Summary:")
        print("This video’s style, tone, and techniques are printed above.")
        print("Use this to understand its editing structure and target audience.\n")

    except Exception as e:
        print(f"❌ Error: {e}")
