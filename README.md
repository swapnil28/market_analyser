# Stock Market Analysis Web App

A complete full-stack web application for tracking BSE/NSE holdings with real-time price data.

**Status**: ✅ Production Ready | Render.com Compatible

---

## 🚀 Quick Start

### Option 1: Run Locally

**Terminal 1 - Backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python seed_data.py
python run.py
```

**Terminal 2 - Frontend**
```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:3000

**Login with:**
- Email: `test@example.com`
- Password: `password123`

---

### Option 2: Deploy to Render.com

1. Push code to GitHub
2. Go to https://render.com
3. Create new "Web Service"
4. Connect GitHub repo
5. Set build command: `cd backend && pip install -r requirements.txt`
6. Set start command: `cd backend && python run.py`
7. Add PostgreSQL database
8. Set environment variables:
   - `JWT_SECRET_KEY=<random-secret>`
   - `DATABASE_URL=<postgres-url>`
   - `FLASK_ENV=production`
9. Deploy!

---

## 📦 What's Included

✅ **Backend** (Flask + SQLAlchemy)
- REST API with 15+ endpoints
- JWT authentication
- PostgreSQL (production) / SQLite (dev)
- CORS enabled

✅ **Frontend** (React + Vite)
- Login/Register pages
- Dashboard with 20 stocks
- Search functionality
- Responsive design
- Chart.js integration

✅ **Database**
- 20 Indian stocks (INFY, TCS, WIPRO, etc.)
- 30 days of OHLCV price data
- User accounts with secure password hashing

---

## 🛠 Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React 18 + Vite + Axios |
| Backend | Flask + SQLAlchemy |
| Database | PostgreSQL (prod) / SQLite (dev) |
| Auth | JWT |
| Deployment | Render.com |

---

## 📁 Project Structure

```
backend/                      # Flask API
├── app/
│   ├── models/               # Database models
│   ├── routes/               # API endpoints
│   └── __init__.py           # App factory
├── run.py                    # Dev server
├── seed_data.py              # Database seed
├── Procfile                  # Deployment config
└── requirements.txt

frontend/                     # React app
├── src/
│   ├── pages/                # Login, Dashboard, etc.
│   ├── components/           # UI components
│   └── services/             # API calls
└── package.json
```

---

## 🔐 Database Models

- **User** - Authentication & profiles
- **Stock** - 20 Indian stocks
- **Price** - OHLCV data (30 days/stock)
- **Portfolio** - User portfolios
- **PortfolioHolding** - Stocks in portfolios
- **Watchlist** - User watchlists
- **WatchlistItem** - Stocks in watchlists

---

## 🔧 Environment Variables

**Backend (.env)**
```
FLASK_ENV=development
DATABASE_URL=sqlite:///stock_db.sqlite
JWT_SECRET_KEY=your-secret-key
PORT=5001
```

**Frontend (.env)**
```
VITE_API_URL=http://localhost:5001
```

---

## 📊 API Endpoints

### Auth
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user

### Stocks
- `GET /stocks` - Get all stocks (paginated)
- `GET /stocks/<ticker>` - Get stock details
- `GET /stocks/<ticker>/prices` - Get price history

### Portfolio
- `GET /portfolio` - Get user portfolios
- `POST /portfolio` - Create portfolio
- `POST /portfolio/<id>/holdings` - Add stock to portfolio

### Watchlist
- `GET /watchlist` - Get user watchlists
- `POST /watchlist` - Create watchlist
- `POST /watchlist/<id>/items` - Add stock to watchlist

---

## 🚀 Deployment

### Render.com Setup

1. **Create PostgreSQL database** (Add-on in Render)
2. **Set environment variables** in Render dashboard:
   ```
   JWT_SECRET_KEY=<generate-random>
   FLASK_ENV=production
   DATABASE_URL=<auto-set-by-render>
   ```
3. **Build Command**
   ```
   cd backend && pip install -r requirements.txt
   ```
4. **Start Command**
   ```
   cd backend && python run.py
   ```

The app will be live at: `https://<your-service>.onrender.com`

---

## ✨ Features

- User authentication (register & login)
- View all 20 stocks with current prices
- Search stocks by ticker or name
- Portfolio management framework
- Watchlist functionality
- Price charts (Chart.js)
- Responsive mobile-friendly UI

---

## 🧪 Testing

```bash
# Test backend endpoints
curl http://localhost:5001/health
curl http://localhost:5001/stocks
curl http://localhost:5001/stocks/INFY
curl http://localhost:5001/stocks/INFY/prices
```

---

## 📝 License

Open source - free for personal and commercial use

---

**Ready to deploy?** → Push to GitHub and connect to Render.com

Built with ❤️ | Flask + React | 2026
