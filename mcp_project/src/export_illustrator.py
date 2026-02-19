import os

def generate_svg_from_features(data):
    svg_content = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <style>
    text {{ font-family: Arial, sans-serif; font-size: 16px; }}
  </style>
  <text x="20" y="40" fill="#6f42c1">🎨 Color & Visual Style:</text>
  <text x="40" y="60">{', '.join(data.get('Color & Visual Style', []))}</text>
  
  <text x="20" y="100" fill="#6f42c1">✨ Transitions & Effects:</text>
  <text x="40" y="120">{', '.join(data.get('Transitions & Effects', []))}</text>

  <text x="20" y="160" fill="#6f42c1">🎥 Camera Work:</text>
  <text x="40" y="180">{', '.join(data.get('Camera Work', []))}</text>

  <text x="20" y="220" fill="#6f42c1">📝 Typography & Text:</text>
  <text x="40" y="240">{', '.join(data.get('Typography & Text', []))}</text>

  <text x="20" y="280" fill="#6f42c1">🤖 AI/Advanced Features:</text>
  <text x="40" y="300">{', '.join(data.get('AI/Advanced Features', []))}</text>

  <text x="20" y="340" fill="#6f42c1">🧠 LLM Summary:</text>
  <text x="40" y="360">{data.get('LLM Summary', '').strip()}</text>
</svg>"""

    path = "static/exported_summary.svg"
    os.makedirs("static", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    return path
