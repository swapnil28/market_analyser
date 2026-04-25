#!/usr/bin/env python
import sys
import os

# Add backend folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
