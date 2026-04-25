from app import db
from datetime import datetime




class PortfolioHolding(db.Model):
    __tablename__ = 'portfolio_holdings'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False, index=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'), nullable=False, index=True)
    quantity = db.Column(db.Float, nullable=False)
    avg_cost = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_current_value(self):
        """Get current market value of this holding."""
        latest_price = self.stock.get_latest_price()
        if latest_price:
            return self.quantity * float(latest_price.close)
        return 0.0

    def get_profit_loss(self):
        """Calculate profit/loss on this holding."""
        return self.get_current_value() - (self.quantity * self.avg_cost)

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'portfolio_id': self.portfolio_id,
            'stock_id': self.stock_id,
            'stock': self.stock.to_dict() if self.stock else None,
            'quantity': float(self.quantity),
            'avg_cost': float(self.avg_cost),
            'current_value': self.get_current_value(),
            'profit_loss': self.get_profit_loss(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self):
        return f'<PortfolioHolding {self.portfolio_id} {self.stock_id}>'
