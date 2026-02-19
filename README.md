# 🎬 MCP Video Inspector – Media Content Processor

An AI-powered system that analyzes YouTube videos and extracts professional video editing features using Computer Vision and LLM-based analysis.

This project is designed to understand how modern edited videos are structured — including color grading, transitions, camera movement, typography, and audio mood — and generate intelligent summaries for creative reuse.

---

## 🚀 Key Features

- 🎨 **Color & Visual Style Detection**
- 🎬 **Transition & Effect Detection**
- 📷 **Camera Movement Analysis**
- 🔤 **Typography & Text Extraction (OCR)**
- 🎵 **Audio Feature & Mood Analysis**
- 🤖 **LLM-Based Editing Summary**
- 🖌️ **SVG Export for Adobe Illustrator**
- 🎨 **Figma Integration Support**
- 📊 Modular AI-based Feature Extraction Pipeline

---

## 🏗️ System Architecture

User Input (YouTube URL)
↓
Video Download
↓
Frame & Audio Extraction (FFmpeg)
↓
Feature Extraction Modules
• Color & Visual Style
• Transitions & Effects
• Camera Work
• Typography (OCR)
• Audio Analysis
↓
LLM-Based Summary (Ollama / LLaMA)
↓
Export to SVG / Figma Template

---

## 🛠️ Tech Stack

### 🔹 Backend

- Python
- Flask

### 🔹 AI & Video Processing

- OpenCV
- SceneDetect
- pytesseract (OCR)
- librosa (Audio Analysis)
- ffmpeg
- Ollama (LLaMA 3)

### 🔹 Frontend

- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

mcp-video-inspector/
│
├── app.py
├── mcp_server.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
├── templates/
├── src/
├── utils/
├── m_server/

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PariBansal/mcp-video-inspector.git
cd mcp-video-inspector
```

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate # Windows

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Install FFmpeg (Important)

This project requires FFmpeg for video and audio processing.

Install FFmpeg separately and add it to system PATH.

Verify installation:
ffmpeg -version

### 5️⃣ Run the Application

python app.py

Open browser and go to:

http://127.0.0.1:5000/

🎯 Use Cases

Video Editing Style Analysis

Content Creator Style Replication

AI-based Editing Insights

Media Research & Study

Template Generation for Designers

Automated Creative Workflow Assistance

🔬 Future Improvements

Real-time Video Analysis

Deployment on Cloud (AWS / Render)

Advanced Transition Classification (ML Model)

Style Similarity Scoring

Multi-video Comparative Analysis

Fine-tuned LLM for Editing Domain

📌 Research & Learning Outcomes

Through this project:

Implemented Computer Vision pipelines

Integrated LLM with media analysis

Built modular AI processing architecture

Designed full-stack AI application

Worked with multimedia processing tools

👩‍💻 Developed By

Pari Bansal
B.Tech CSE (AI & ML)
K.R. Mangalam University

⭐ If You Like This Project

Feel free to star the repository and contribute!
