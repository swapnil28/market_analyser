#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app, db

app = create_app()
