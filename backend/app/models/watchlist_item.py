from app import db
from datetime import datetime




class WatchlistItem(db.Model):
    __tablename__ = 'watchlist_items'

    id = db.Column(db.Integer, primary_key=True)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'), nullable=False, index=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'), nullable=False, index=True)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'watchlist_id': self.watchlist_id,
            'stock_id': self.stock_id,
            'stock': self.stock.to_dict() if self.stock else None,
            'added_at': self.added_at.isoformat() if self.added_at else None,
        }

    def __repr__(self):
        return f'<WatchlistItem {self.watchlist_id} {self.stock_id}>'
