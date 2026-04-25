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
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    frontend_dist = os.path.join(base_dir, '..', 'frontend', 'dist')
    index_path = os.path.join(frontend_dist, 'index.html')

    app = Flask(__name__, static_folder=frontend_dist, static_url_path='')

    # Config
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints FIRST (so they take priority)
    from app.routes import register_blueprints
    register_blueprints(app)

    # Serve React frontend (catch-all, must be LAST)
    @app.route('/')
    def index():
        if os.path.exists(index_path):
            return send_from_directory(frontend_dist, 'index.html')
        return jsonify({'error': 'Frontend not built'}), 404

    @app.route('/<path:path>')
    def serve_static(path):
        # Skip API routes (they're handled by blueprints)
        if path.startswith('api/') or path.startswith('health') or path.startswith('auth') or path.startswith('stocks'):
            return jsonify({'error': 'Not found'}), 404
        # Serve static files from dist
        full_path = os.path.join(frontend_dist, path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            return send_from_directory(frontend_dist, path)
        # Return index.html for all other routes (React Router)
        if os.path.exists(index_path):
            return send_from_directory(frontend_dist, 'index.html')
        return jsonify({'error': 'Not found'}), 404

    # Create tables
    with app.app_context():
        db.create_all()

    return app
