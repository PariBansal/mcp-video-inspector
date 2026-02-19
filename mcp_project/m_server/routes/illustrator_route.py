# mcp_server/routes/illustrator_route.py

from flask import Blueprint, request, jsonify
from src.illustrator_integration import upload_to_illustrator

bp = Blueprint("illustrator", __name__, url_prefix="/illustrator")

@bp.route("/upload", methods=["POST"])
def illustrator_upload():
    try:
        content = request.get_json()
        if not content:
            return jsonify({"error": "No JSON body received"}), 400

        upload_to_illustrator(content)

        return jsonify({"status": "✅ Upload simulated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
