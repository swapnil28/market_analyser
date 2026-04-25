def register_blueprints(app):
    """Register all route blueprints with the Flask app."""
    from .health import health_bp
    from .auth import auth_bp
    from .stocks import stocks_bp
    from .portfolio import portfolio_bp
    from .watchlist import watchlist_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(stocks_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(watchlist_bp)
