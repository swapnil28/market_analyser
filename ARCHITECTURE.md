# Architecture Documentation

Complete technical architecture of the Stock Market Analysis application.

---

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    User's Browser (Port 3000)                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           React SPA (Vite)                           │   │
│  │  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │   │
│  │  │   Pages     │  │  Components  │  │  Services  │  │   │
│  │  │  (5 pages)  │  │   (5 comps)  │  │  (API)     │  │   │
│  │  └─────────────┘  └──────────────┘  └────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓ HTTPS
                     (REST API calls)
                            ↓
┌─────────────────────────────────────────────────────────────┐
│               Flask Backend (Port 5001)                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Flask App Factory                                   │   │
│  │  ├─ JWT Authentication (Flask-JWT-Extended)         │   │
│  │  ├─ CORS enabled                                    │   │
│  │  └─ 5 Route Blueprints (health, auth, stocks, etc)  │   │
│  │                                                      │   │
│  │  Routes (15+ endpoints):                            │   │
│  │  ├─ health.py      (GET /health)                    │   │
│  │  ├─ auth.py        (POST login, register, GET me)   │   │
│  │  ├─ stocks.py      (GET stocks, search, prices)     │   │
│  │  ├─ portfolio.py   (CRUD portfolios & holdings)     │   │
│  │  └─ watchlist.py   (CRUD watchlists & items)        │   │
│  └──────────────────────────────────────────────────────┘   │
│                            ↓
│  ┌──────────────────────────────────────────────────────┐   │
│  │  SQLAlchemy ORM (7 Models)                           │   │
│  │  ├─ User            (email, password_hash)           │   │
│  │  ├─ Stock           (ticker, name, exchange)         │   │
│  │  ├─ Price           (OHLCV data, date)              │   │
│  │  ├─ Portfolio       (user portfolios)                │   │
│  │  ├─ PortfolioHolding (stocks in portfolio)           │   │
│  │  ├─ Watchlist       (user watchlists)                │   │
│  │  └─ WatchlistItem   (stocks in watchlist)            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              PostgreSQL Database (Render)                    │
│              OR SQLite Database (Local Dev)                  │
│                                                              │
│  Tables (7):                                                │
│  ├─ users (4 cols)       [1 record - test user]            │
│  ├─ stocks (4 cols)      [20 records - Indian stocks]      │
│  ├─ prices (9 cols)      [600 records - 30 days × 20]      │
│  ├─ portfolios (5 cols)  [0 records - user-created]        │
│  ├─ portfolio_holdings   [0 records - user-created]        │
│  ├─ watchlists (5 cols)  [0 records - user-created]        │
│  └─ watchlist_items      [0 records - user-created]        │
└─────────────────────────────────────────────────────────────┘
```

---

## Frontend Architecture (React 18 + Vite)

### Entry Point
```
index.html → src/main.jsx → src/App.jsx (Router)
```

### Routing (React Router v6)
```
/login          → Login.jsx (public)
/dashboard      → Dashboard.jsx (protected)
/stock/:ticker  → StockDetail.jsx (protected)
/portfolio      → Portfolio.jsx (protected)
/watchlist      → Watchlist.jsx (protected)
/               → Home (redirects based on auth)
```

### Pages (5)

1. **Login.jsx** (Public)
   - Email/password login form
   - Pre-filled test credentials
   - Stores JWT token in localStorage
   - Redirects to dashboard on success

2. **Dashboard.jsx** (Protected)
   - Grid of 20 stocks (12 per page)
   - Real-time search (debounced)
   - Pagination controls
   - Click to view stock details

3. **StockDetail.jsx** (Protected)
   - Stock name, ticker, exchange
   - Current price display
   - 30-day price chart (Chart.js)
   - OHLCV data table

4. **Portfolio.jsx** (Protected)
   - List user portfolios
   - Total value & cost basis
   - Number of holdings per portfolio
   - Framework for adding stocks

5. **Watchlist.jsx** (Protected)
   - List user watchlists
   - Items per watchlist
   - Stock ticker + name per item
   - Framework for managing items

### Components (5 reusable)

1. **NavBar.jsx**
   - Logo/home link
   - Navigation links (Dashboard, Portfolio, Watchlist)
   - User email display
   - Logout button
   - Sticky positioning

2. **StockCard.jsx**
   - Ticker + exchange badge
   - Stock name
   - Current price in rupees
   - View details button
   - Hover effects

3. **SearchBar.jsx**
   - Text input with debouncing
   - Real-time search on stocks
   - Search icon indicator
   - Responsive width

4. **PriceChart.jsx**
   - Line chart using Chart.js
   - 30-day close prices
   - Responsive sizing
   - Tooltip on hover

5. **NavBar.jsx** (Plus NavBar CSS)
   - Styled with purple gradient
   - Mobile-responsive menu
   - User info section

### State Management
- Auth state in App.jsx (lifted)
- Page-level state in each page component
- API calls through Axios service layer
- JWT token stored in localStorage

### API Integration (Axios)
```
src/services/api.js
├─ authAPI.login()
├─ authAPI.register()
├─ authAPI.getCurrentUser()
├─ stocksAPI.getStocks()
├─ stocksAPI.getStock()
├─ stocksAPI.getStockPrices()
├─ portfolioAPI.getPortfolios()
├─ portfolioAPI.createPortfolio()
├─ portfolioAPI.getPortfolio()
├─ portfolioAPI.addHolding()
├─ watchlistAPI.getWatchlists()
├─ watchlistAPI.createWatchlist()
├─ watchlistAPI.getWatchlist()
└─ watchlistAPI.addItem()
```

---

## Backend Architecture (Flask + SQLAlchemy)

### Application Factory Pattern
```
backend/app/__init__.py

create_app():
  ├─ Load environment variables
  ├─ Initialize Flask instance
  ├─ Configure from config.py
  ├─ Init extensions (SQLAlchemy, JWT, CORS)
  ├─ Register blueprints (5 routes)
  ├─ Serve React frontend (index.html fallback)
  ├─ Create database tables
  └─ Return app instance
```

### Entry Point
```
backend/run.py
├─ Create app using factory
├─ Get PORT from environment (default 5001)
├─ Create all database tables
└─ Start Flask development server
```

### Configuration (config.py)
```
Config (base)
├─ SQLALCHEMY_TRACK_MODIFICATIONS = False
├─ JWT_SECRET_KEY = (from env)
├─ JWT_ACCESS_TOKEN_EXPIRES = 30 days
└─ DATABASE_URL = (from env or SQLite)

DevelopmentConfig
├─ DEBUG = True
└─ DATABASE_URL = sqlite:///stock_db.sqlite

ProductionConfig
├─ DEBUG = False
└─ DATABASE_URL = postgresql://... (from Render)

TestingConfig
└─ DATABASE_URI = sqlite:///:memory:
```

### Route Blueprints (5)

**1. health.py**
```
GET /health → {"status": "healthy", "message": "..."}
```

**2. auth.py**
```
POST /auth/register
├─ Request: {email, password, first_name?, last_name?}
└─ Response: {user, message}

POST /auth/login
├─ Request: {email, password}
└─ Response: {access_token, user, message}

GET /auth/me (protected)
└─ Response: {user}
```

**3. stocks.py**
```
GET /stocks?page=1&per_page=20&search=INFY
└─ Response: {stocks[], total, pages, current_page}

GET /stocks/<ticker>
└─ Response: {stock}

GET /stocks/<ticker>/prices?days=30
└─ Response: {ticker, name, prices[]}
```

**4. portfolio.py**
```
GET /portfolio (protected)
└─ Response: {portfolios[]}

POST /portfolio (protected)
├─ Request: {name, description?}
└─ Response: {portfolio}

GET /portfolio/<id> (protected)
└─ Response: {portfolio}

POST /portfolio/<id>/holdings (protected)
├─ Request: {stock_id, quantity, avg_cost}
└─ Response: {holding}
```

**5. watchlist.py**
```
GET /watchlist (protected)
└─ Response: {watchlists[]}

POST /watchlist (protected)
├─ Request: {name, description?}
└─ Response: {watchlist}

GET /watchlist/<id> (protected)
└─ Response: {watchlist}

POST /watchlist/<id>/items (protected)
├─ Request: {stock_id}
└─ Response: {item}
```

### Database Models (7)

**1. User**
```python
id (PK)
email (unique)
password_hash (bcrypt)
first_name
last_name
created_at
updated_at
↓ relationships
portfolios []
watchlists []
```

**2. Stock**
```python
id (PK)
ticker (unique, index)
name
exchange (NSE/BSE)
created_at
↓ relationships
prices []
portfolio_holdings []
watchlist_items []
↓ methods
get_latest_price() → Price
```

**3. Price**
```python
id (PK)
stock_id (FK, index)
date (with stock_id = unique)
open, high, low, close (Float)
volume (BigInteger)
created_at
↓ relationships
stock → Stock
```

**4. Portfolio**
```python
id (PK)
user_id (FK, index)
name
description
created_at
updated_at
↓ relationships
holdings []
↓ methods
get_total_value() → float
get_total_cost() → float
```

**5. PortfolioHolding**
```python
id (PK)
portfolio_id (FK, index)
stock_id (FK, index)
quantity (Float)
avg_cost (Float)
created_at
updated_at
↓ relationships
portfolio → Portfolio
stock → Stock
↓ methods
get_current_value() → float
get_profit_loss() → float
```

**6. Watchlist**
```python
id (PK)
user_id (FK, index)
name
description
created_at
updated_at
↓ relationships
items []
```

**7. WatchlistItem**
```python
id (PK)
watchlist_id (FK, index)
stock_id (FK, index)
added_at
↓ relationships
watchlist → Watchlist
stock → Stock
```

### Authentication (JWT)

**Login Flow:**
```
POST /auth/login
├─ Find user by email
├─ Verify password (check_password_hash)
├─ Create access token (identity=user.id)
├─ Store token in browser localStorage
└─ Frontend sends in Authorization header

Subsequent Requests:
├─ Send: Authorization: Bearer <token>
├─ JWT validates (check expiry, signature)
├─ Extract user_id from token
└─ Proceed with request
```

**Protected Routes:**
```
@jwt_required()  # Decorator on route
├─ Validates token
├─ Extracts user_id
└─ Returns 401 if invalid
```

---

## Data Flow Examples

### Login Flow
```
1. User enters test@example.com / password123
2. Frontend: POST /auth/login
3. Backend: User.query.filter_by(email).first()
4. Backend: user.check_password(password) ✓
5. Backend: create_access_token(identity=user.id)
6. Backend: Return {access_token, user}
7. Frontend: localStorage.setItem('token', token)
8. Frontend: Navigate to /dashboard
9. App.jsx fetches /auth/me with token
10. Dashboard displays user email
```

### View Stocks Flow
```
1. User clicks "Dashboard"
2. Frontend: GET /stocks?page=1&per_page=12
3. Backend: Query stocks with pagination
4. Backend: For each stock, get latest price
5. Backend: Return {stocks[], total, pages}
6. Frontend: Display stock cards (grid)
7. User clicks stock card
8. Frontend: Navigate to /stock/INFY
9. Frontend: GET /stocks/INFY + GET /stocks/INFY/prices
10. Backend: Return stock details + 30-day prices
11. Frontend: Display price chart + OHLCV table
```

### Add to Watchlist Flow
```
1. User logged in, viewing stock INFY
2. User clicks "Add to Watchlist" button
3. Frontend: POST /watchlist (if first time)
   - Request: {name: "My Stocks"}
   - Response: {watchlist}
4. Frontend: POST /watchlist/<id>/items
   - Request: {stock_id: 1}
   - Response: {item}
5. Backend: Create WatchlistItem record
6. Frontend: Show success message
7. Frontend: Navigate to /watchlist
8. Frontend: GET /watchlist
9. Backend: Return watchlists with items
10. Frontend: Display watchlist with INFY added
```

---

## Deployment Architecture (Render.com)

```
┌─────────────────────────────────────────────┐
│  Render.com (Hosting Platform)              │
│                                             │
│  ┌────────────────────────────────────┐   │
│  │ Web Service (Flask Backend)        │   │
│  │ ├─ Python 3.12.3                  │   │
│  │ ├─ Port: Dynamic (provided by     │   │
│  │ │        Render environment)      │   │
│  │ ├─ Build: pip install requirements│   │
│  │ ├─ Start: gunicorn app:create_app │   │
│  │ └─ Auto-scales, sleeps after 15min│   │
│  └────────────────────────────────────┘   │
│           ↓ (connects to)                  │
│  ┌────────────────────────────────────┐   │
│  │ PostgreSQL Database                │   │
│  │ ├─ Version: Latest                 │   │
│  │ ├─ Storage: 100 MB (free tier)     │   │
│  │ ├─ Auto-backups enabled            │   │
│  │ └─ Internal URL: postgresql://...  │   │
│  └────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
         ↑ (user accesses via HTTPS)
    https://<service>.onrender.com
         ↓ (served by)
  ┌──────────────────────┐
  │ React Frontend       │
  │ (dist/ folder)       │
  │ Compiled JavaScript  │
  └──────────────────────┘
```

---

## Technology Stack

### Frontend
| Tech | Version | Purpose |
|------|---------|---------|
| React | 18.2.0 | UI framework |
| Vite | 4.4.5 | Build tool (instant HMR) |
| React Router | 6.14.0 | Client-side routing |
| Axios | 1.4.0 | HTTP client |
| Chart.js | 3.9.1 | Price charts |
| React Chart.js 2 | 5.2.0 | Chart component wrapper |

### Backend
| Tech | Version | Purpose |
|------|---------|---------|
| Flask | 2.3.3 | Web framework |
| Flask-SQLAlchemy | 3.0.5 | ORM |
| SQLAlchemy | 2.0.35 | Database abstraction |
| Flask-JWT-Extended | 4.5.2 | JWT authentication |
| Flask-CORS | 4.0.0 | Cross-origin requests |
| Werkzeug | 2.3.7 | WSGI utilities |
| psycopg2-binary | 2.9.7 | PostgreSQL driver |
| Gunicorn | 21.2.0 | Production server |

### Database
- **Development**: SQLite (file-based, no setup)
- **Production**: PostgreSQL (managed by Render)

---

## Security Features

1. **Password Hashing**
   - Werkzeug generate_password_hash (PBKDF2)
   - check_password_hash for verification

2. **JWT Authentication**
   - HS256 signature algorithm
   - 30-day expiration
   - User ID encoded in token

3. **CORS**
   - Frontend domain: http://localhost:3000 (dev)
   - Backend domain: https://<service>.onrender.com (prod)
   - Allows credentialed requests

4. **Database Relationships**
   - User isolation (users only see their portfolios/watchlists)
   - Foreign key constraints
   - Cascade delete for data integrity

---

## Performance Considerations

1. **Database Queries**
   - Stock with get_latest_price() uses lazy import to avoid circular imports
   - Pagination on stocks list (12 per page)
   - Index on (stock_id, date) for price queries

2. **Frontend Optimization**
   - Vite provides instant HMR during development
   - Production build: tree-shaking, minification
   - React Router lazy loading (framework ready)
   - Search debouncing on Dashboard

3. **Caching**
   - Browser caches static assets (dist folder)
   - No server-side caching (simple architecture)
   - Can add Redis for future optimization

---

## Scalability Path

**Current (Small)**: Single backend, single database
↓
**Medium**: Add caching layer (Redis)
↓
**Large**: Microservices (user service, stock service, etc.)
↓
**Enterprise**: Event streaming (Kafka), data warehouse

---

Built with ❤️ | Flask + React | 2026
