# m_server/server.py

from flask import Flask
from m_server.routes import analyze_route, illustrator_route
from flask_cors import CORS  # type: ignore # Optional: allows front-end or MCP clients to connect

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    # Register route blueprints
    app.register_blueprint(analyze_route.bp)
    app.register_blueprint(illustrator_route.bp)

    @app.route("/")
    def index():
        return {"message": "✅ MCP API Server Running"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)  # Flask will run on http://127.0.0.1:8000
