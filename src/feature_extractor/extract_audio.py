# src/feature_extractor/extract_audio.py
import subprocess
import os
import shutil

def extract_audio_with_ffmpeg(input_video_path: str, output_audio_path: str) -> str:
    """
    Extracts audio from a video using FFmpeg.

    Args:
        input_video_path (str): Path to the input video.
        output_audio_path (str): Path to save the extracted audio (.wav).

    Returns:
        str: Path to the extracted audio file, or error message.
    """
    print("🔄 Extracting audio using FFmpeg...")

    # Absolute paths
    input_video_path = os.path.abspath(input_video_path)
    output_audio_path = os.path.abspath(output_audio_path)

    # Prefer system ffmpeg, fallback to local one
    ffmpeg_cmd = shutil.which("ffmpeg")
    if not ffmpeg_cmd:
        local_ffmpeg = os.path.abspath("ffmpeg.exe")
        if os.path.exists(local_ffmpeg):
            ffmpeg_cmd = local_ffmpeg
            print("📦 Using bundled ffmpeg.exe")
        else:
            error = "❌ FFmpeg not found (neither system nor local)"
            print(error)
            return error

    command = [
        ffmpeg_cmd,
        "-y",
        "-i", input_video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        output_audio_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"✅ Audio file saved to: {output_audio_path}")
        return output_audio_path
    except subprocess.CalledProcessError as e:
        error = f"❌ FFmpeg execution failed: {str(e)}"
        print(error)
        return error
