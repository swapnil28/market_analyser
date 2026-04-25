#!/usr/bin/env python
import os
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)
