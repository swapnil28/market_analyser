#!/usr/bin/env python
"""Seed database with test data."""
import os
from datetime import datetime, timedelta
from app import create_app, db
from app.models.user import User
from app.models.stock import Stock
from app.models.price import Price

app = create_app()

# Indian stocks data
STOCKS_DATA = [
    ('INFY', 'Infosys Limited', 'NSE'),
    ('TCS', 'Tata Consultancy Services', 'NSE'),
    ('WIPRO', 'Wipro Limited', 'NSE'),
    ('HCL', 'HCL Technologies', 'NSE'),
    ('RELIANCE', 'Reliance Industries', 'NSE'),
    ('HDFC', 'HDFC Bank', 'NSE'),
    ('ICICI', 'ICICI Bank', 'NSE'),
    ('AXIS', 'Axis Bank', 'NSE'),
    ('ITC', 'ITC Limited', 'NSE'),
    ('NESTLEIND', 'Nestle India', 'NSE'),
    ('MARUTI', 'Maruti Suzuki', 'NSE'),
    ('BAJAJ-AUTO', 'Bajaj Auto', 'NSE'),
    ('TATASTEEL', 'Tata Steel', 'NSE'),
    ('HINDALCO', 'Hindalco Industries', 'NSE'),
    ('SBIN', 'State Bank of India', 'NSE'),
    ('BHARTIARTL', 'Bharti Airtel', 'NSE'),
    ('JIOSYSTEMS', 'Jio Systems', 'NSE'),
    ('POWERGRID', 'Power Grid Corporation', 'NSE'),
    ('NTPC', 'NTPC Limited', 'NSE'),
    ('SUNPHARMA', 'Sun Pharmaceutical', 'NSE'),
]

PRICE_BASE = {
    'INFY': 1096.0,
    'TCS': 3850.0,
    'WIPRO': 518.0,
    'HCL': 1642.0,
    'RELIANCE': 2956.0,
    'HDFC': 2687.0,
    'ICICI': 1058.0,
    'AXIS': 1015.0,
    'ITC': 452.0,
    'NESTLEIND': 25200.0,
    'MARUTI': 9850.0,
    'BAJAJ-AUTO': 9180.0,
    'TATASTEEL': 148.0,
    'HINDALCO': 732.0,
    'SBIN': 607.0,
    'BHARTIARTL': 1267.0,
    'JIOSYSTEMS': 1856.0,
    'POWERGRID': 312.0,
    'NTPC': 310.0,
    'SUNPHARMA': 895.0,
}


def seed_database():
    """Seed database with initial data."""
    with app.app_context():
        # Check if data exists
        if User.query.first():
            print("Database already seeded. Skipping...")
            return

        print("Seeding database...")

        # Create test user
        user = User(email='test@example.com', first_name='Test', last_name='User')
        user.set_password('password123')
        db.session.add(user)
        db.session.flush()

        print(f"Created test user: {user.email}")

        # Create stocks and price history
        base_date = datetime.now().date() - timedelta(days=30)

        for ticker, name, exchange in STOCKS_DATA:
            stock = Stock(ticker=ticker, name=name, exchange=exchange)
            db.session.add(stock)
            db.session.flush()

            # Generate 30 days of price data
            base_price = PRICE_BASE[ticker]
            for i in range(30):
                price_date = base_date + timedelta(days=i)

                # Simulate price variation (±5%)
                variation = (i % 3 - 1) * 0.02  # -2%, 0%, +2%
                close_price = base_price * (1 + variation)

                price = Price(
                    stock_id=stock.id,
                    date=price_date,
                    open=close_price * 0.98,
                    high=close_price * 1.02,
                    low=close_price * 0.96,
                    close=close_price,
                    volume=5000000 + (i * 100000),
                )
                db.session.add(price)

        db.session.commit()
        print(f"Created {len(STOCKS_DATA)} stocks with 30 days of price data")
        print("Database seeding complete!")


if __name__ == '__main__':
    seed_database()
