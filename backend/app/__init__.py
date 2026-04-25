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

    # IMPORTANT: Register frontend routes FIRST (before blueprints)
    # This ensures static files and React routes are served before API routes
    @app.route('/')
    def serve_index():
        """Serve index.html"""
        return send_from_directory(frontend_dist, 'index.html')

    @app.route('/<path:path>')
    def serve_frontend(path):
        """Serve static files or fallback to index.html for React Router"""
        file_path = os.path.join(frontend_dist, path)

        # Serve static file if it exists
        if os.path.isfile(file_path):
            return send_from_directory(frontend_dist, path)

        # Otherwise serve index.html (React Router will handle it)
        return send_from_directory(frontend_dist, 'index.html')

    # Register blueprints AFTER frontend routes
    from app.routes import register_blueprints
    register_blueprints(app)


    # Error handler for 404 - serve index.html for React Router
    @app.errorhandler(404)
    def not_found(error):
        """Serve index.html for all 404s (React Router handling)"""
        if os.path.exists(index_path):
            return send_from_directory(frontend_dist, 'index.html')
        return jsonify({'error': 'Not found'}), 404

    # Create tables
    with app.app_context():
        db.create_all()

    return app
