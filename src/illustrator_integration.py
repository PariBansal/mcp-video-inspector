# src/illustrator_integration.py

import os
import subprocess

def upload_to_illustrator(features: dict, selected_keys: list):
    """
    Simulated export of features to Adobe Illustrator.
    In reality, this will launch Illustrator and attempt to open a placeholder export file.
    """
    print("\n🎨 Preparing data for Adobe Illustrator...")

    # Prepare export content
    export_lines = []
    for category in selected_keys:
        value = features.get(category, None)
        if value:
            export_lines.append(f"\n🗂️  [ {category.upper()} ]")
            if isinstance(value, list):
                for item in value:
                    export_lines.append(f"   • {item}")
            elif isinstance(value, dict):
                for k, v in value.items():
                    export_lines.append(f"   • {k}: {v}")
            else:
                export_lines.append(f"   • {value}")

    export_text = "\n".join(export_lines)

    # Save to text file
    output_path = "illustrator_output.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(export_text)

    print("✅ Feature export saved to illustrator_output.txt")

    # ✅ Automatically open Illustrator with the file (ensure the path is correct!)
    illustrator_path = r"C:\Program Files\Adobe\Adobe Illustrator 2024\Support Files\Contents\Windows\Illustrator.exe"
    if os.path.exists(illustrator_path):
        try:
            subprocess.Popen([illustrator_path, os.path.abspath(output_path)])
            print("🚀 Sent to Illustrator")
        except Exception as e:
            print(f"⚠️ Unable to open Illustrator automatically: {e}")
    else:
        print("⚠️ Illustrator path not found. Please verify the path or open the file manually.")
