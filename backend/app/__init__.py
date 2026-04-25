from flask import Flask, send_from_directory, send_file, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    """Application factory."""
    # Get absolute paths
    # __file__ = /path/to/backend/app/__init__.py
    # dirname(__file__) = /path/to/backend/app
    # dirname(dirname(__file__)) = /path/to/backend
    # We need /path/to/frontend/dist, so go up one more level from backend
    app_dir = os.path.dirname(os.path.abspath(__file__))  # backend/app
    backend_dir = os.path.dirname(app_dir)  # backend
    root_dir = os.path.dirname(backend_dir)  # root (project root)
    frontend_dist = os.path.join(root_dir, 'frontend', 'dist')
    index_path = os.path.join(frontend_dist, 'index.html')

    app = Flask(__name__)

    # Config
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints FIRST (so they take priority)
    from app.routes import register_blueprints
    register_blueprints(app)

    # DEBUG: Log paths on startup
    print(f"=== STARTUP DEBUG ===")
    print(f"frontend_dist = {frontend_dist}")
    print(f"index_path = {index_path}")
    print(f"frontend_dist exists? {os.path.exists(frontend_dist)}")
    print(f"index_path exists? {os.path.exists(index_path)}")
    if os.path.exists(frontend_dist):
        print(f"frontend_dist contents: {os.listdir(frontend_dist)}")
    print(f"=== END DEBUG ===\n")

    # Serve React frontend
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        """Serve frontend files or index.html for React Router"""
        print(f"[SERVE] path={path}, frontend_dist={frontend_dist}")

        # For root path or no extension, serve index.html
        if not path or not os.path.splitext(path)[1]:
            print(f"[SERVE] Serving index.html for root/no-extension path")
            try:
                return send_from_directory(frontend_dist, 'index.html')
            except Exception as e:
                print(f"[SERVE] Error serving index.html: {e}")
                return jsonify({'error': str(e)}), 500

        # Try to serve the file
        file_path = os.path.join(frontend_dist, path)
        if os.path.isfile(file_path):
            print(f"[SERVE] Serving file: {path}")
            return send_from_directory(frontend_dist, path)

        # If file doesn't exist, serve index.html (for React Router)
        print(f"[SERVE] File not found, serving index.html for React Router")
        return send_from_directory(frontend_dist, 'index.html')

    # Create tables
    with app.app_context():
        db.create_all()

    return app
