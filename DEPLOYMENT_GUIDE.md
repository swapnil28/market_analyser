# Render.com Deployment Guide

Complete step-by-step guide to deploy your Stock Market Analysis app to Render.com for free.

---

## Prerequisites

1. GitHub account (with code pushed)
2. Render.com account (free tier available)
3. PostgreSQL database (included with Render free tier)

---

## Step 1: Prepare Your Code for Deployment

### 1.1 Build the Frontend

```bash
cd frontend
npm install
npm run build
```

This creates the compiled frontend in `frontend/dist/`.

### 1.2 Commit Everything to Git

```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

---

## Step 2: Create Render Service

1. Go to https://render.com
2. Sign in with GitHub
3. Click **"New +"** → **"Web Service"**
4. Select your `stock-market-app` repository
5. Fill in:
   - **Name**: `stock-market-app`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install -r requirements.txt && npm install && npm run build`
   - **Start Command**: `cd backend && python run.py`
   - **Plan**: Free (unlimited)

---

## Step 3: Add PostgreSQL Database

1. In your Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Set:
   - **Name**: `stock-market-db`
   - **Database**: `stock_db`
   - **User**: `postgres`
   - **Plan**: Free (included)
3. Click **"Create Database"**
4. Copy the **Internal Database URL**

---

## Step 4: Configure Environment Variables

In your Web Service settings, go to **"Environment"** and add:

```
JWT_SECRET_KEY=your-random-secret-key-here
FLASK_ENV=production
DATABASE_URL=<paste-postgres-url-here>
```

**Generate a secure JWT secret:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Step 5: Seed the Database

After deployment, seed the database with test data:

```bash
# SSH into Render
render ssh stock-market-app

# Run seed script
cd backend
python seed_data.py

# Create test user
curl -X POST http://localhost:5001/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

Or use the deployment webhook to auto-seed.

---

## Step 6: Deploy!

1. Click **"Deploy"** in Render dashboard
2. Wait for build to complete (2-5 minutes)
3. Your app is live at: `https://<your-service>.onrender.com`

---

## Testing Your Deployment

```bash
# Test health endpoint
curl https://<your-service>.onrender.com/health

# Login
curl -X POST https://<your-service>.onrender.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Get stocks
curl https://<your-service>.onrender.com/stocks \
  -H "Authorization: Bearer <token>"
```

---

## Troubleshooting

**App won't start?**
- Check Render logs: Dashboard → Logs tab
- Verify `requirements.txt` is up to date
- Ensure `PORT` environment variable is set (not needed for Render, but won't hurt)

**Database connection error?**
- Check `DATABASE_URL` in environment variables
- Verify PostgreSQL service is running
- Ensure database URL uses `postgresql://` not `postgres://`

**Frontend not loading?**
- Run `npm run build` before pushing
- Verify `frontend/dist/` is committed and tracked
- Check that build command includes frontend build

**Login not working?**
- Verify test user was seeded with `seed_data.py`
- Check JWT_SECRET_KEY is set correctly
- Look at server logs for error details

---

## Environment Variables Summary

| Variable | Value | Example |
|----------|-------|---------|
| `JWT_SECRET_KEY` | Random secret | `AbCdEfGhIjKlMnOpQrStUvWxYz123456` |
| `FLASK_ENV` | `production` | `production` |
| `DATABASE_URL` | PostgreSQL URL | `postgresql://user:pass@host:5432/db` |
| `PORT` | Port number | `5001` (Render sets automatically) |

---

## File Structure for Deployment

```
.
├── backend/
│   ├── app/
│   ├── run.py
│   ├── seed_data.py
│   ├── requirements.txt
│   ├── Procfile              ← Used by Render
│   ├── runtime.txt           ← Python version
│   └── .env.example
├── frontend/
│   ├── src/
│   ├── dist/                 ← Must be built before deployment
│   ├── package.json
│   └── .env
└── README.md
```

---

## Optional: Auto-Seed on Deploy

Create `backend/post_deploy.py`:

```python
from app import create_app, db
from seed_data import seed_database

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_database()
    print("Database seeded!")
```

Update **Start Command** in Render:
```
cd backend && python post_deploy.py && python run.py
```

---

## Free Tier Limits

- **Compute**: 0.5 CPU, 512 MB RAM
- **Database**: 100 MB storage, 1 MB/month bandwidth
- **Spins down** after 15 min of inactivity (takes ~30 sec to wake)

For production, upgrade to paid tier.

---

## What's Next?

After deployment:
1. Create real portfolios and watchlists
2. Add real stock price data via API
3. Implement price alerts
4. Add social features
5. Deploy mobile app

---

**Live URL**: https://<your-service>.onrender.com
**Admin Email**: test@example.com
**Admin Password**: password123

Built with ❤️ | Flask + React | 2026
