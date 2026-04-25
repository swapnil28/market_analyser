from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(200), nullable=False)
    exchange = db.Column(db.String(10))  # NSE or BSE
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    prices = db.relationship('Price', backref='stock', lazy=True, cascade='all, delete-orphan')
    portfolio_holdings = db.relationship('PortfolioHolding', backref='stock', lazy=True)
    watchlist_items = db.relationship('WatchlistItem', backref='stock', lazy=True)

    def get_latest_price(self):
        """Get the most recent price record for this stock."""
        from .price import Price
        return Price.query.filter_by(stock_id=self.id).order_by(Price.date.desc()).first()

    def to_dict(self, include_prices=False):
        """Convert to dictionary."""
        latest_price = self.get_latest_price()
        data = {
            'id': self.id,
            'ticker': self.ticker,
            'name': self.name,
            'exchange': self.exchange,
            'current_price': float(latest_price.close) if latest_price else 0.0,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        if include_prices:
            data['prices'] = [p.to_dict() for p in self.prices]
        return data

    def __repr__(self):
        return f'<Stock {self.ticker}>'
