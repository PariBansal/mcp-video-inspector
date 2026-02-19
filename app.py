from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

from src.video_downloader import download_video
from src.feature_extractor.color_style import extract as extract_color_style
from src.feature_extractor.transitions_effects import extract as extract_transitions_effects
from src.feature_extractor.camera_work import extract as extract_camera_work
from src.feature_extractor.typography_text import extract as extract_typography
from src.feature_extractor.ai_advanced_effects import extract as extract_ai_features

load_dotenv()
app = Flask(__name__)

latest_result = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/figma")
def figma_editor():
    selected = latest_result.get("Selected Features", {})
    # Ensure fallback if not found
    default_selected = {
        "Primary Color": selected.get("Primary Color", "Not Detected"),
        "Typography": selected.get("Typography", "Not Detected"),
        "Transition": selected.get("Transition", "Not Detected"),
        "Camera Style": selected.get("Camera Style", "Not Detected"),
        "Audio Design": selected.get("Audio Design", "Not Detected"),
        "AI Effects": selected.get("AI Effects", "Not Detected")
    }
    return render_template("figma.html", selected_features=default_selected)

@app.route("/analyze", methods=["POST"])
def analyze():
    global latest_result
    url = request.json.get("url", "").strip()
    result = {
        "Color & Visual Style": [],
        "Transitions & Effects": [],
        "Camera Work": [],
        "Typography & Text": [],
        "AI/Advanced Features": [],
        "LLM Summary": "",
        "Selected Features": {},
        "error": ""
    }

    try:
        video_path = download_video(url, "downloads")
        if not video_path:
            raise Exception("Video download failed.")

        result["Color & Visual Style"] = extract_color_style(video_path)
        result["Transitions & Effects"] = extract_transitions_effects(video_path)
        result["Camera Work"] = extract_camera_work(video_path)
        result["Typography & Text"] = extract_typography(video_path)
        result["AI/Advanced Features"] = extract_ai_features(video_path)

        # Save only top suggestions for now
        result["Selected Features"] = {
            "Primary Color": result["Color & Visual Style"][0] if result["Color & Visual Style"] else "Not Detected",
            "Typography": result["Typography & Text"][0] if result["Typography & Text"] else "Not Detected",
            "Transition": result["Transitions & Effects"][0] if result["Transitions & Effects"] else "Not Detected",
            "Camera Style": result["Camera Work"][0] if result["Camera Work"] else "Not Detected",
            "AI Effects": result["AI/Advanced Features"][0] if result["AI/Advanced Features"] else "Not Detected"
        }

        # Generate summary
        summary_input = f"""
        Color & Visual Style: {result['Color & Visual Style']}
        Transitions & Effects: {result['Transitions & Effects']}
        Camera Work: {result['Camera Work']}
        Typography & Text: {result['Typography & Text']}
        AI/Advanced Features: {result['AI/Advanced Features']}
        """

        llama_response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": f"You are a video editor. Based on this:\n{summary_input}\nSummarize editing style and tone.",
            "stream": False
        })

        if llama_response.status_code == 200:
            result["LLM Summary"] = llama_response.json()["response"]
        else:
            result["error"] = f"Ollama error: {llama_response.text}"

        latest_result = result

    except Exception as e:
        result["error"] = str(e)

    return jsonify(result)

@app.route("/selected-features", methods=["POST"])
def selected_features():
    selected = request.json.get("features", {})
    # Only update the selected portion, not entire result
    if "Selected Features" in latest_result:
        latest_result["Selected Features"].update(selected)
    else:
        latest_result["Selected Features"] = selected

    return render_template("figma.html", selected_features=latest_result["Selected Features"])

if __name__ == "__main__":
    app.run(debug=True)
