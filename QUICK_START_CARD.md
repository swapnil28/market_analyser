# Quick Start Card - 7-Step Deployment

**Print this or bookmark it. Copy & paste commands exactly as shown.**

---

## STEP 1: Open in Visual Studio

```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render
code .
```

**Check**: VS opens with project folder visible ✓

---

## STEP 2: Audit Project Structure

**In Claude Code**, paste this prompt:

```
PROJECT STRUCTURE AUDIT

Base: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

Check:
- backend/app/models/ → 7 files (user, stock, price, portfolio, holding, watchlist, watchlist_item)
- backend/app/routes/ → 5 files (health, auth, stocks, portfolio, watchlist)
- backend/ → app/__init__.py has create_app()
- requirements.txt → has Flask, SQLAlchemy, gunicorn
- Procfile → web: gunicorn "app:create_app()"
- runtime.txt → python-3.12.3
- frontend/package.json → has react, vite, axios, chart.js
- frontend/src/pages/ → 5 JSX files
- frontend/src/components/ → 5 JSX files
- Documentation → README, DEPLOYMENT_GUIDE, ARCHITECTURE files

Report: ✅ if pass, ⚠️ if issues
```

**Check**: All ✅ (no ⚠️) ✓

---

## STEP 3: Build Frontend

```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/frontend

npm install
# Wait 2-3 minutes...

npm run build
# Should show: ✓ built in X.XXs
```

**Check**: 
- `npm install` completes ✓
- `npm run build` shows ✓ built ✓
- `frontend/dist/` folder exists ✓
- `frontend/dist/index.html` exists ✓

---

## STEP 4: Verify Backend Render-Ready

**In Claude Code**, paste this prompt:

```
RENDER COMPATIBILITY CHECK

Base: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/backend

Verify:
1. runtime.txt = python-3.12.3
2. Procfile = web: gunicorn "app:create_app()"
3. requirements.txt has: Flask, SQLAlchemy==2.0.35, psycopg2-binary, gunicorn
4. app/__init__.py has create_app() function
5. app/config.py reads DATABASE_URL and JWT_SECRET_KEY from env

Report: ✅ if all pass
```

**Check**: All ✅ ✓

---

## STEP 5: Commit & Push to GitHub

```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

git status
# Should show changes (frontend/dist/ and any edits)

git add .

git status
# Should show: "Changes to be committed"

git commit -m "Build: Frontend compiled for production, ready for Render deployment"

git push origin main
# Should show: "✓" and "main -> main"
```

**Check**: 
- `git status` clean ✓
- `git commit` succeeds ✓
- `git push` succeeds ✓
- No "rejected" or "conflict" messages ✓

---

## STEP 6: Deploy to Render.com

**Browser-based (no terminal)**

### 6.1 Create Web Service
```
Go to: https://dashboard.render.com
Click: "New +"
Select: "Web Service"
Choose: "stock-market-app" repo

Fill:
- Name: stock-market-app
- Environment: Python 3
- Build Command: cd backend && pip install -r requirements.txt
- Start Command: cd backend && python run.py
- Plan: Free

Click "Create Web Service"
```

**Wait**: 2-5 minutes for build to complete. Shows "Deployed" (green) ✓

### 6.2 Create PostgreSQL Database
```
Click: "New +"
Select: "PostgreSQL"

Fill:
- Name: stock-market-db
- Database: stock_db
- User: postgres
- Plan: Free

Click "Create Database"
```

**Copy**: Internal Database URL (will be shown after creation)

### 6.3 Set Environment Variables

In Web Service → Environment:

```
KEY: JWT_SECRET_KEY
VALUE: (run in terminal: python3 -c "import secrets; print(secrets.token_urlsafe(32))")
     Copy output → paste as VALUE

KEY: FLASK_ENV
VALUE: production

KEY: DATABASE_URL
VALUE: (paste the PostgreSQL Internal Database URL from 6.2)
```

**Check**: 
- Web Service created ✓
- PostgreSQL created ✓
- 3 env vars set ✓
- Status shows "Deployed" (green) ✓

---

## STEP 7: Test Live App

### Test 7.1: Health Check
```
Open browser:
https://stock-market-app.onrender.com/health

Expected:
{
  "status": "healthy",
  "message": "Stock Market API is running"
}
```

✓ **If you see JSON response, app is running!**

### Test 7.2: Frontend Load
```
Open browser:
https://stock-market-app.onrender.com

Expected: Login form appears
```

✓ **If you see login page, frontend works!**

### Test 7.3: Login
```
Email: test@example.com
Password: password123

Click Login
```

✓ **If dashboard shows 20 stocks, database is seeded!**

### Test 7.4: Stock Detail
```
Click any stock (e.g., INFY)
```

✓ **If chart and prices appear, API works!**

### Test 7.5: Search
```
Type "TCS" in search
```

✓ **If results filter, search works!**

---

## ✅ DEPLOYMENT COMPLETE!

**Your app is live at:**
```
https://stock-market-app.onrender.com
```

**Test credentials:**
```
Email: test@example.com
Password: password123
```

---

## 🆘 If Something Fails

| Problem | Check |
|---------|-------|
| Step 3 fails | `node --version` (should be 16+) |
| Step 5 fails | `git remote -v` (check URL) |
| Step 6 fails | Render logs → "Logs" tab |
| Step 7 fails | Render logs for errors |
| Stocks don't show | Need to seed DB (see below) |

### Seed Database (if stocks missing)

In Render dashboard → Web Service → "Shell" tab:

```bash
cd backend
python seed_data.py

# Should show: "Database seeding complete!"
```

Then refresh browser.

---

## 📚 Full Documentation

- `README.md` - Project overview
- `CLAUDE_CODE_WORKFLOW.md` - Detailed 7-step guide
- `CLAUDE_CODE_PROMPTS.md` - Copy/paste prompts for Claude Code
- `DEPLOYMENT_GUIDE.md` - Render.com guide
- `ARCHITECTURE.md` - Technical details

---

## ⏱️ Timeline

| Step | Time |
|------|------|
| 1 | 1 min |
| 2 | 2 min |
| 3 | 5 min |
| 4 | 2 min |
| 5 | 2 min |
| 6 | 5 min |
| 7 | 5 min |
| **Total** | **22 min** |

---

**Questions?** Check CLAUDE_CODE_PROMPTS.md for detailed prompts to use in Claude Code.

Built with ❤️ | Claude Code | 2026
