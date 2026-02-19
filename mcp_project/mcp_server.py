# mcp_server.py

from fastmcp import FastMCP  # ✅ This is from the fastmcp package

from src.video_downloader import download_video
from src.video_analyzer import analyze_video
from src.llm_summary import summarize_features
from src.illustrator_integration import upload_to_illustrator

mcp = FastMCP("MCP Video Tool")  # Title visible in Inspector

@mcp.tool()
def process_youtube_video(youtube_url: str) -> dict:
    video_path = download_video(youtube_url, f"downloads/{youtube_url.split('=')[-1]}.mp4")
    features = analyze_video(video_path, video_path.replace(".mp4", ".wav"))
    summary = summarize_features(features)
    return {"features": features, "summary": summary}

@mcp.tool()
def upload_features_to_illustrator(features: dict) -> str:
    upload_to_illustrator(features)
    return "Upload to Illustrator simulated"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=3001)  # ✅ This enables the MCP Inspector
