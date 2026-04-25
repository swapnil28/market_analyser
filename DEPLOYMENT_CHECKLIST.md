# Deployment Checklist - Mark Off As You Complete Each Step

**Print this or check off items as you complete them**

---

## PRE-DEPLOYMENT SETUP

### Claude Code & Tools Setup
- [ ] Visual Studio installed (`code --version` shows version)
- [ ] Node.js installed (`node --version` shows 16+)
- [ ] Git configured (`git config user.name` shows your name)
- [ ] Claude Code installed (`claude-code --version` works)
- [ ] Render.com account created and GitHub connected
- [ ] PostgreSQL knowledge (basic understanding)

---

## STEP 1: Open Project in Visual Studio

**Time: 1 minute**

### Commands
```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render
code .
```

### Verification
- [ ] VS Code opens with project
- [ ] Left sidebar shows: `backend/`, `frontend/`, `README.md`, etc.
- [ ] Terminal visible at bottom
- [ ] Ready to proceed

---

## STEP 2: Audit Project Structure

**Time: 2 minutes**

### In Claude Code
Paste Prompt 2A from CLAUDE_CODE_PROMPTS.md

### Verification
- [ ] Backend models: ✅ 7 files
- [ ] Backend routes: ✅ 5 files
- [ ] Requirements.txt: ✅ all dependencies
- [ ] Procfile: ✅ correct format
- [ ] Runtime.txt: ✅ python-3.12.3
- [ ] Frontend files: ✅ all present
- [ ] Documentation: ✅ all files

**Status**: ✅ ALL GREEN before proceeding

---

## STEP 3: Build Frontend

**Time: 5 minutes**

### Command 1: Install dependencies
```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/frontend
npm install
```

### Verification for npm install
- [ ] Command completes without errors
- [ ] Shows: "added XXX packages in XXXs"
- [ ] No "ERR!" messages
- [ ] Takes 2-3 minutes

### Command 2: Build for production
```bash
npm run build
```

### Verification for npm build
- [ ] Shows: "✓ built in X.XXs"
- [ ] `frontend/dist/` folder created
- [ ] `frontend/dist/index.html` exists (> 1 KB)
- [ ] `frontend/dist/assets/` has .js and .css files
- [ ] No errors in terminal

**Status**: ✅ FRONTEND BUILT before proceeding

---

## STEP 4: Verify Backend for Render

**Time: 2 minutes**

### In Claude Code
Paste Prompt 4A from CLAUDE_CODE_PROMPTS.md

### Verification
- [ ] runtime.txt: ✅ python-3.12.3
- [ ] Procfile: ✅ gunicorn configured
- [ ] requirements.txt: ✅ versions match
- [ ] app/__init__.py: ✅ create_app() function
- [ ] app/config.py: ✅ env variables handled

**Status**: ✅ BACKEND RENDER-READY before proceeding

---

## STEP 5: Commit & Push to GitHub

**Time: 2 minutes**

### Command 1: Check status
```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render
git status
```

### Verification for git status
- [ ] Shows "Changes not staged" or "Untracked files"
- [ ] Lists `frontend/dist/` changes
- [ ] No error messages
- [ ] Ready to add

### Command 2: Add changes
```bash
git add .
```

### Verification for git add
- [ ] Command completes silently (no output = success)
- [ ] No error messages

### Command 3: Verify staging
```bash
git status
```

### Verification for staged changes
- [ ] Shows "Changes to be committed"
- [ ] Lists files being committed
- [ ] frontend/dist/ visible

### Command 4: Commit
```bash
git commit -m "Build: Frontend compiled for production, ready for Render deployment"
```

### Verification for commit
- [ ] Shows number of files changed
- [ ] Shows insertions/deletions
- [ ] No errors

### Command 5: Push to GitHub
```bash
git push origin main
```

### Verification for git push
- [ ] Shows "To https://github.com/YOUR_USERNAME/stock-market-app.git"
- [ ] Shows "main -> main"
- [ ] No "rejected" or "conflict" messages
- [ ] Completes in < 30 seconds

**Status**: ✅ CODE ON GITHUB before proceeding

---

## STEP 6: Deploy to Render.com

**Time: 5 minutes**

### 6.1 Create Web Service

**Browser**: https://dashboard.render.com

- [ ] Click "New +"
- [ ] Select "Web Service"
- [ ] Select your "stock-market-app" repository
- [ ] Fill Name: `stock-market-app`
- [ ] Fill Environment: `Python 3`
- [ ] Fill Build Command: `cd backend && pip install -r requirements.txt`
- [ ] Fill Start Command: `cd backend && python run.py`
- [ ] Select Plan: `Free`
- [ ] Click "Create Web Service"

### Verification for Web Service
- [ ] Service created successfully
- [ ] Shows "Building..." in dashboard
- [ ] Waits 2-5 minutes
- [ ] Changes to "Deployed" (green status)
- [ ] Generate live URL: `https://stock-market-app.onrender.com` (or similar)

### 6.2 Create PostgreSQL Database

**Browser**: Still in render.com dashboard

- [ ] Click "New +"
- [ ] Select "PostgreSQL"
- [ ] Fill Name: `stock-market-db`
- [ ] Fill Database: `stock_db`
- [ ] Fill User: `postgres`
- [ ] Select Plan: `Free`
- [ ] Click "Create Database"

### Verification for PostgreSQL
- [ ] Database created successfully
- [ ] Shows "Available" status (green)
- [ ] Copy "Internal Database URL" (starts with `postgresql://`)
- [ ] Save this URL for Step 6.3

### 6.3 Set Environment Variables

**Browser**: In Web Service settings

- [ ] Go to Web Service (not database)
- [ ] Click "Environment"
- [ ] Click "Add Environment Variable"

**Variable 1: JWT_SECRET_KEY**
```bash
# In your terminal, run:
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Copy the output (43-char base64 string)
```

- [ ] KEY: `JWT_SECRET_KEY`
- [ ] VALUE: (paste the 43-char string)
- [ ] Click "Add"

**Variable 2: FLASK_ENV**
- [ ] KEY: `FLASK_ENV`
- [ ] VALUE: `production`
- [ ] Click "Add"

**Variable 3: DATABASE_URL**
- [ ] KEY: `DATABASE_URL`
- [ ] VALUE: (paste the PostgreSQL URL from 6.2)
- [ ] Click "Add"

### Verification for Environment Variables
- [ ] 3 variables visible in dashboard
- [ ] JWT_SECRET_KEY: ✅ set
- [ ] FLASK_ENV: ✅ production
- [ ] DATABASE_URL: ✅ postgresql:// format
- [ ] Web Service auto-redeploys (may take 1-2 minutes)

**Status**: ✅ DEPLOYED on Render before testing

---

## STEP 7: Test Live App

**Time: 5 minutes**

### 7.1 Health Check

**Browser**:
```
https://stock-market-app.onrender.com/health
```

### Verification
- [ ] Page loads (not 404)
- [ ] Shows JSON: `{"status": "healthy", ...}`
- [ ] No error messages

**If this passes**: Backend is working ✅

### 7.2 Frontend Load

**Browser**:
```
https://stock-market-app.onrender.com
```

### Verification
- [ ] Page loads
- [ ] Shows Login form
- [ ] Email field visible
- [ ] Password field visible
- [ ] Login button visible
- [ ] No console errors (DevTools → Console tab)

**If this passes**: Frontend is working ✅

### 7.3 Login Test

**Browser**: On login page

- [ ] Click email field
- [ ] Type: `test@example.com`
- [ ] Click password field
- [ ] Type: `password123`
- [ ] Click "Login" button

### Verification
- [ ] Page changes (no error)
- [ ] Redirects to `/dashboard`
- [ ] Shows grid of stock cards
- [ ] See "20" stocks (or close to 20)
- [ ] Each card shows: ticker, name, price

**If this passes**: Database & authentication working ✅

### 7.4 Stock Detail Test

**Browser**: On dashboard

- [ ] Click any stock card (e.g., INFY)
- [ ] Wait for page to load

### Verification
- [ ] Stock detail page loads
- [ ] Shows ticker & name at top
- [ ] Shows current price
- [ ] Shows price chart (line graph)
- [ ] Shows OHLCV table below
- [ ] Table has 30 rows (30 days of data)

**If this passes**: Price data & charts working ✅

### 7.5 Search Test

**Browser**: Back on dashboard

- [ ] Click search bar
- [ ] Type: `TCS`
- [ ] Wait 1 second for results

### Verification
- [ ] Grid updates
- [ ] Shows only TCS stock (1 card)
- [ ] Clear search field (backspace or X)
- [ ] Grid shows all 20 stocks again

**If this passes**: Search working ✅

---

## POST-DEPLOYMENT CHECKLIST

### Confirm Live
- [ ] App is live at: `https://stock-market-app.onrender.com`
- [ ] Login works: `test@example.com` / `password123`
- [ ] Dashboard shows 20 stocks
- [ ] Stock detail shows chart & prices
- [ ] Search filters stocks
- [ ] No errors in browser console

### Share Access
- [ ] URL: `https://stock-market-app.onrender.com`
- [ ] Email: `test@example.com`
- [ ] Password: `password123`
- [ ] Shared with stakeholders ✅

### Future Maintenance
- [ ] Render dashboard bookmarked
- [ ] Monitor logs weekly
- [ ] Scale up if needed (switch from Free tier)

---

## 🎉 DEPLOYMENT COMPLETE!

**All steps finished?**

- [ ] Step 1: ✅ Opened in VS
- [ ] Step 2: ✅ Audited structure
- [ ] Step 3: ✅ Built frontend
- [ ] Step 4: ✅ Verified backend
- [ ] Step 5: ✅ Pushed to GitHub
- [ ] Step 6: ✅ Deployed to Render
- [ ] Step 7: ✅ Tested live app
- [ ] Post-deployment: ✅ Confirmed working

---

## 🚨 IF SOMETHING FAILS

**Check this in order:**

### 7.1 Health endpoint fails (404 or no response)
1. [ ] Check Render Web Service status (green = deployed)
2. [ ] Check Render logs for errors
3. [ ] Check runtime.txt = python-3.12.3
4. [ ] Check Procfile is correct
5. [ ] Redeploy: git push again

### 7.3 Login fails or dashboard blank
1. [ ] Check if database was seeded
2. [ ] Check Render logs for database errors
3. [ ] Check DATABASE_URL is set correctly
4. [ ] SSH into Render and run: `python seed_data.py`
5. [ ] Try login again

### 7.4 Stock detail shows no chart
1. [ ] Check browser DevTools → Network tab
2. [ ] Verify `/stocks/INFY/prices` endpoint returns data
3. [ ] Check if Chart.js loaded
4. [ ] Check Render logs

### 7.5 Search not working
1. [ ] Check browser console for JS errors
2. [ ] Try different search term
3. [ ] Check API endpoint in Render logs
4. [ ] Clear browser cache and retry

---

**Total Time**: ~22 minutes from start to live deployment ✅

**Next Step**: Share your live URL with team or stakeholders!

Built with ❤️ | Claude Code | 2026
