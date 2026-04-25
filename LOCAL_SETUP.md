# Local Development Setup

Complete guide to run the Stock Market Analysis app locally on your machine.

---

## Prerequisites

- Python 3.12+
- Node.js 16+ (with npm)
- Git

---

## Step 1: Clone and Navigate

```bash
git clone <your-repo-url>
cd Market_Analizer_render
```

---

## Step 2: Set Up Backend

### 2.1 Create Virtual Environment

```bash
cd backend
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 2.2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.3 Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:
```
FLASK_ENV=development
DATABASE_URL=sqlite:///stock_db.sqlite
JWT_SECRET_KEY=dev-secret-key-12345
PORT=5001
```

### 2.4 Seed Database with Test Data

```bash
python seed_data.py
```

Output should show:
```
Seeding database...
Created test user: test@example.com
Created 20 stocks with 30 days of price data
Database seeding complete!
```

### 2.5 Start Backend Server

```bash
python run.py
```

You should see:
```
 * Serving Flask app
 * Debug mode: off
 * Running on http://0.0.0.0:5001
```

---

## Step 3: Set Up Frontend (New Terminal)

### 3.1 Install Dependencies

```bash
cd frontend
npm install
```

### 3.2 Start Development Server

```bash
npm run dev
```

You should see:
```
VITE v4.4.5  ready in 234 ms

➜  Local:   http://localhost:3000/
```

---

## Step 4: Access the App

Open your browser: **http://localhost:3000**

**Login with:**
- Email: `test@example.com`
- Password: `password123`

---

## Project Directory Structure

```
Market_Analizer_render/
├── backend/
│   ├── app/
│   │   ├── models/               # Database models (7 models)
│   │   │   ├── user.py
│   │   │   ├── stock.py
│   │   │   ├── price.py
│   │   │   ├── portfolio.py
│   │   │   ├── holding.py
│   │   │   ├── watchlist.py
│   │   │   └── watchlist_item.py
│   │   ├── routes/               # API endpoints (5 blueprints)
│   │   │   ├── health.py
│   │   │   ├── auth.py
│   │   │   ├── stocks.py
│   │   │   ├── portfolio.py
│   │   │   └── watchlist.py
│   │   ├── config.py             # Environment config
│   │   └── __init__.py           # Flask app factory
│   ├── run.py                    # Development server entry point
│   ├── seed_data.py              # Database initialization
│   ├── requirements.txt          # Python dependencies
│   ├── Procfile                  # Production deployment config
│   ├── runtime.txt               # Python version (3.12.3)
│   └── .env.example              # Environment template
│
├── frontend/
│   ├── src/
│   │   ├── pages/                # Page components
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── StockDetail.jsx
│   │   │   ├── Portfolio.jsx
│   │   │   └── Watchlist.jsx
│   │   ├── components/           # Reusable UI components
│   │   │   ├── NavBar.jsx
│   │   │   ├── StockCard.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   └── PriceChart.jsx
│   │   ├── services/
│   │   │   └── api.js            # Axios API client
│   │   ├── App.jsx               # Root component with routing
│   │   ├── main.jsx              # Entry point
│   │   └── index.css             # Global styles
│   ├── index.html                # HTML template
│   ├── package.json              # Node dependencies
│   ├── vite.config.js            # Vite configuration
│   └── .env                      # Frontend API URL config
│
├── README.md                     # Project overview
├── LOCAL_SETUP.md                # This file
├── DEPLOYMENT_GUIDE.md           # Render.com deployment steps
└── .gitignore
```

---

## Database Schema

### Models (7 total)

1. **User** - User accounts with password hashing
2. **Stock** - 20 Indian stocks (INFY, TCS, WIPRO, etc.)
3. **Price** - OHLCV data (30 days per stock, 600 records total)
4. **Portfolio** - User portfolios (empty by default)
5. **PortfolioHolding** - Stocks in portfolios (empty by default)
6. **Watchlist** - User watchlists (empty by default)
7. **WatchlistItem** - Stocks in watchlists (empty by default)

### Test Data

**20 Stocks Included:**
```
INFY, TCS, WIPRO, HCL, RELIANCE, HDFC, ICICI, AXIS, ITC, NESTLEIND,
MARUTI, BAJAJ-AUTO, TATASTEEL, HINDALCO, SBIN, BHARTIARTL, JIOSYSTEMS,
POWERGRID, NTPC, SUNPHARMA
```

**30 Days of Price Data** per stock with realistic OHLCV values

---

## API Endpoints (15+ total)

### Health Check
- `GET /health` - Service status

### Authentication (3)
- `POST /auth/register` - Create account
- `POST /auth/login` - Login, get JWT token
- `GET /auth/me` - Current user info

### Stocks (3)
- `GET /stocks?page=1&per_page=20&search=` - All stocks with pagination
- `GET /stocks/<ticker>` - Stock details
- `GET /stocks/<ticker>/prices?days=30` - Price history

### Portfolio (4)
- `GET /portfolio` - User portfolios
- `POST /portfolio` - Create portfolio
- `GET /portfolio/<id>` - Portfolio details
- `POST /portfolio/<id>/holdings` - Add stock to portfolio

### Watchlist (4)
- `GET /watchlist` - User watchlists
- `POST /watchlist` - Create watchlist
- `GET /watchlist/<id>` - Watchlist details
- `POST /watchlist/<id>/items` - Add stock to watchlist

---

## Common Commands

### Backend Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Install new package
pip install package-name
pip freeze > requirements.txt

# Run migrations (if using Alembic)
flask db init
flask db migrate
flask db upgrade

# Start development server
python run.py

# Run seed script again (clears and repopulates DB)
python seed_data.py
```

### Frontend Commands

```bash
# Install new package
npm install package-name
npm install --save-dev package-name

# Build for production
npm run build

# Preview production build
npm run preview

# Clean build
rm -rf node_modules dist
npm install
npm run build
```

### Database Commands

```bash
# Remove and recreate database
rm backend/instance/stock_db.sqlite
python backend/seed_data.py

# Access SQLite database
sqlite3 backend/instance/stock_db.sqlite
sqlite> .tables
sqlite> SELECT COUNT(*) FROM stocks;
sqlite> .quit
```

---

## Testing Endpoints

### With curl

```bash
# Health check
curl http://localhost:5001/health

# Get all stocks
curl http://localhost:5001/stocks

# Login
curl -X POST http://localhost:5001/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Get authenticated stock data (replace TOKEN)
curl http://localhost:5001/stocks/INFY \
  -H "Authorization: Bearer TOKEN"

# Get price history
curl http://localhost:5001/stocks/INFY/prices \
  -H "Authorization: Bearer TOKEN"
```

### With Postman

1. Create new collection
2. Set base URL: `http://localhost:5001`
3. Create requests for each endpoint
4. For protected routes, add header: `Authorization: Bearer {token}`

---

## Troubleshooting

### Backend Issues

**Port 5001 already in use:**
```bash
# Find and kill process using port 5001
lsof -i :5001
kill -9 <PID>

# Or change PORT in .env
PORT=5002
```

**ModuleNotFoundError: No module named 'flask'**
```bash
# Ensure venv is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Database locked error:**
```bash
# Delete and reseed database
rm backend/instance/stock_db.sqlite
python backend/seed_data.py
```

### Frontend Issues

**Port 3000 already in use:**
```bash
# Kill process on port 3000
lsof -i :3000
kill -9 <PID>

# Vite will use next available port
npm run dev
```

**VITE_API_URL not working:**
- Verify `frontend/.env` has correct backend URL
- Restart frontend dev server
- Check browser DevTools > Network tab for API calls

**Blank stocks table:**
- Verify backend is running (check http://localhost:5001/health)
- Verify test user was created and logged in
- Check browser console for errors
- Verify `seed_data.py` ran without errors

---

## Best Practices

1. **Always activate venv** before running Python commands
2. **Keep dependencies updated** with `pip freeze`
3. **Test both locally and in production** before going live
4. **Back up your database** before major changes
5. **Use environment variables** for secrets, not hardcoded values
6. **Commit frequently** with clear commit messages

---

## Next Steps

After verifying local setup:
1. Create a GitHub repository
2. Push all files to GitHub
3. Follow `DEPLOYMENT_GUIDE.md` to deploy to Render.com
4. Set up continuous deployment (auto-deploy on push)

---

**Need help?**
- Check logs: `python run.py` shows Flask logs
- Browser console: DevTools > Console tab
- Network tab: DevTools > Network tab shows API calls
- Database: `sqlite3 backend/instance/stock_db.sqlite`

Built with ❤️ | Flask + React | 2026
