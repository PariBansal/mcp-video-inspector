# src/video_downloader.py

import os
import yt_dlp

def download_video(url, output_path="downloads"):
    try:
        print(f"📥 Downloading video from: {url}")
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get("title", None)
            ext = info_dict.get("ext", "mp4")
            downloaded_path = os.path.join(output_path, f"{video_title}.{ext}")
            print(f"✅ Downloaded to: {downloaded_path}")
            return downloaded_path

    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None
