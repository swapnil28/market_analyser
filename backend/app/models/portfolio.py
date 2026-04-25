from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    holdings = db.relationship('PortfolioHolding', backref='portfolio', lazy=True, cascade='all, delete-orphan')

    def get_total_value(self):
        """Calculate total portfolio value based on current prices."""
        total = 0.0
        for holding in self.holdings:
            latest_price = holding.stock.get_latest_price()
            if latest_price:
                total += holding.quantity * float(latest_price.close)
        return total

    def get_total_cost(self):
        """Calculate total cost basis."""
        return sum(holding.quantity * holding.avg_cost for holding in self.holdings)

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'total_value': self.get_total_value(),
            'total_cost': self.get_total_cost(),
            'holdings': [h.to_dict() for h in self.holdings],
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self):
        return f'<Portfolio {self.name}>'
