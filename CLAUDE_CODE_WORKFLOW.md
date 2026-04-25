# Claude Code Workflow - Stock Market App Deployment

Complete step-by-step guide to build and deploy using Claude Code + Visual Studio + Render.com

**Target**: Build → Deploy → Test LIVE (no localhost)

---

## Prerequisites Check

### 1. Visual Studio Setup
```bash
# Open Terminal in your Visual Studio
# Or use Command Palette: Ctrl+` (backtick)

# Verify VS is installed
code --version
# Expected output: 1.xx.xx or higher
```

### 2. Claude Code Installation & Configuration

**Step A: Install Claude Code CLI**
```bash
# On macOS/Linux
npm install -g @anthropic-ai/claude-code

# On Windows (PowerShell as Admin)
npm install -g @anthropic-ai/claude-code

# Verify installation
claude-code --version
```

**Step B: Authenticate Claude Code**
```bash
# Initialize Claude Code
claude-code init

# This will prompt you to:
# 1. Enter your Anthropic API key
# 2. Set your preferred workspace directory
```

**Step C: Configure for Your Project**
```bash
# Navigate to your project folder
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

# Create Claude Code config file
cat > .claudecode.json << 'EOF'
{
  "project_name": "stock-market-app",
  "description": "Stock Market Analysis Web App",
  "target_platform": "render",
  "github_repo": "stock-market-app",
  "root_directory": "."
}
EOF
```

### 3. GitHub Account Verification
```bash
# Verify git is configured
git config --global user.email
git config --global user.name

# If not configured, set it:
git config --global user.email "swapnil.nikam@gmail.com"
git config --global user.name "Swapnil Nikam"
```

### 4. Render.com Account
- ✅ Already created (from previous work)
- ✅ GitHub connected
- Ready to deploy

---

## 7-Step Deployment Process

### **STEP 1: Initialize Project in Visual Studio**

**Objective**: Open project in VS and prepare for Claude Code workflow

**Exact Commands** (Copy & Paste):

```bash
# 1.1 Navigate to project
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

# 1.2 Open in Visual Studio
code .

# Expected: VS opens with project folder visible on left sidebar
```

**Verification Checklist**:
- [ ] VS opens the project
- [ ] File tree shows: `backend/`, `frontend/`, `README.md`, etc.
- [ ] Terminal at bottom shows correct path

**If stuck**: 
```bash
# Check if VS Code is in PATH
which code

# If not found, install CLI tools in VS:
# Command Palette (Cmd+Shift+P) → "Shell Command: Install 'code' command in PATH"
```

---

### **STEP 2: Verify Project Structure with Claude Code**

**Objective**: Use Claude Code to audit file structure before deployment

**Exact Prompt for Claude Code**:

```
PROJECT AUDIT PROMPT:

You are auditing a Stock Market Analysis app for Render.com deployment.

Current directory: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

Tasks:
1. List all files in backend/app/models/ - must have 7 files
2. List all files in backend/app/routes/ - must have 5 files
3. Verify backend/requirements.txt exists and contains: Flask, SQLAlchemy, Flask-JWT-Extended, psycopg2-binary, gunicorn
4. Verify frontend/package.json exists and contains: react, vite, axios, chart.js
5. Verify README.md, LOCAL_SETUP.md, DEPLOYMENT_GUIDE.md exist
6. Check .gitignore exists

Report:
- ✅ if file count matches
- ⚠️ if any file missing
- ❌ if structure incorrect

Only report findings, do NOT create or modify files.
```

**How to Run in Claude Code**:
```bash
# In VS Terminal:
claude-code audit --project-structure

# Or manually invoke with prompt above in Claude Code chat
```

**Expected Output**:
```
✅ Backend models: 7 files found
✅ Backend routes: 5 files found
✅ Requirements.txt: all dependencies present
✅ Package.json: all dependencies present
✅ Documentation: 3 files found
✅ .gitignore: exists
```

**If any ❌**: Stop and fix before moving to Step 3

---

### **STEP 3: Build Frontend for Production**

**Objective**: Compile React app for deployment (no localhost needed)

**Exact Commands**:

```bash
# 3.1 Navigate to frontend
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/frontend

# 3.2 Install dependencies (first time only)
npm install

# Expected output: "added XXX packages in XXXs"
# This takes 2-3 minutes

# 3.3 Build for production
npm run build

# Expected output:
# ✓ built in 2.34s
# dist/
#   ├── index.html
#   ├── assets/
#   │   ├── index-XXXXX.js
#   │   └── index-XXXXX.css
```

**Verification Checklist**:
- [ ] `npm install` completes without errors
- [ ] `npm run build` shows "✓ built" message
- [ ] `frontend/dist/` folder exists
- [ ] `frontend/dist/index.html` exists (≥1 KB)
- [ ] `frontend/dist/assets/` has .js and .css files

**If build fails**:
```bash
# Clear cache and retry
rm -rf node_modules package-lock.json
npm install
npm run build
```

---

### **STEP 4: Prepare Backend for Render Deployment**

**Objective**: Verify backend is Render-compatible

**Exact Prompt for Claude Code**:

```
BACKEND DEPLOYMENT CHECK:

Target: Render.com (Python 3.12.3)
Directory: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/backend

Verify:
1. runtime.txt exists and contains: python-3.12.3
2. Procfile exists and contains: web: gunicorn "app:create_app()"
3. requirements.txt has all these (exact versions):
   - Flask==2.3.3
   - Flask-SQLAlchemy==3.0.5
   - SQLAlchemy==2.0.35
   - Flask-JWT-Extended==4.5.2
   - psycopg2-binary==2.9.7
4. app/__init__.py has create_app() function
5. app/config.py handles DATABASE_URL and JWT_SECRET_KEY from environment

If ANY item missing or incorrect:
- Report what's wrong
- Do NOT fix, just report

If ALL items correct:
- Report: "✅ BACKEND RENDER-READY"
```

**How to Run**:
```bash
# In VS Terminal, from project root:
claude-code verify --backend --render

# Or check manually:
cat backend/runtime.txt
cat backend/Procfile
grep -E "Flask|SQLAlchemy|gunicorn" backend/requirements.txt
```

**Expected Output**:
```
✅ runtime.txt: python-3.12.3
✅ Procfile: gunicorn configured
✅ requirements.txt: all dependencies correct
✅ app/__init__.py: create_app() exists
✅ app/config.py: environment variables handled
✅ BACKEND RENDER-READY
```

**If any ⚠️**: Report the issue before Step 5

---

### **STEP 5: Commit & Push to GitHub**

**Objective**: Push built app to GitHub (Render will auto-deploy)

**Exact Commands**:

```bash
# 5.1 Navigate to project root
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

# 5.2 Check git status
git status

# Expected: frontend/dist/ should be visible (if not committed before)
# Should show modified files only, no untracked files

# 5.3 Add all changes
git add .

# 5.4 Check what will be committed
git status

# Expected output example:
# On branch main
# Changes to be committed:
#   new file: frontend/dist/index.html
#   new file: frontend/dist/assets/index-XXXXX.js
#   ...

# 5.5 Commit with clear message
git commit -m "Build: Frontend compiled for production, ready for Render deployment"

# 5.6 Push to GitHub
git push origin main

# Expected output:
# Enumerating objects: XX, done.
# Writing objects: 100% (XX/XX), XXX KiB | XXX KiB/s, done.
# To https://github.com/YOUR_USERNAME/stock-market-app.git
#    xxxxxxx..xxxxxxx  main -> main
```

**Verification Checklist**:
- [ ] `git status` shows no errors
- [ ] `git add .` completes
- [ ] `git commit` shows files being committed
- [ ] `git push` succeeds (no auth errors)
- [ ] No "rejected" or "conflict" messages

**If push fails**:
```bash
# Check remote URL
git remote -v

# Should show: https://github.com/YOUR_USERNAME/stock-market-app.git

# If auth fails, try:
git config --global credential.helper osxkeychain  # macOS
# or
git config --global credential.helper wincred  # Windows
```

---

### **STEP 6: Deploy to Render.com**

**Objective**: Trigger Render to build and deploy from GitHub

**Exact Steps** (Browser-based):

**6.1 Go to Render Dashboard**
```
URL: https://dashboard.render.com
```

**6.2 Create New Web Service**
```
1. Click "New +"
2. Select "Web Service"
3. Select your "stock-market-app" repository
4. Fill in:
   - Name: stock-market-app
   - Environment: Python 3
   - Build Command: cd backend && pip install -r requirements.txt
   - Start Command: cd backend && python run.py
   - Plan: Free
```

**6.3 Add PostgreSQL Database**
```
1. Click "New +"
2. Select "PostgreSQL"
3. Fill in:
   - Name: stock-market-db
   - Database: stock_db
   - User: postgres
4. Click "Create Database"
5. Copy the "Internal Database URL"
```

**6.4 Set Environment Variables**
```
In Web Service Settings → Environment:

Add these:
KEY: JWT_SECRET_KEY
VALUE: (run this in terminal: python3 -c "import secrets; print(secrets.token_urlsafe(32))")

KEY: FLASK_ENV
VALUE: production

KEY: DATABASE_URL
VALUE: (paste the PostgreSQL Internal Database URL from Step 6.3)
```

**6.5 Deploy**
```
Click "Create Web Service"

Expected: Deploy starts automatically
- Build stage: 2-5 minutes
- Shows "Building..." then "Deployed"
```

**Verification Checklist**:
- [ ] Web Service created successfully
- [ ] PostgreSQL database created
- [ ] 3 environment variables set
- [ ] Render shows "Deployed" status (green)
- [ ] Live URL shows: https://stock-market-app.onrender.com (or similar)

**If deployment fails**:
```
Check Render Logs:
1. Go to Web Service
2. Click "Logs" tab
3. Look for error messages
4. Common issues:
   - Python version mismatch (should be 3.12.3)
   - Missing dependencies in requirements.txt
   - DATABASE_URL malformed
```

---

### **STEP 7: Test Live App on Render**

**Objective**: Verify app works end-to-end without localhost

**Exact Tests** (Browser-based):

**7.1 Health Check**
```
URL: https://stock-market-app.onrender.com/health

Expected Response:
{
  "status": "healthy",
  "message": "Stock Market API is running"
}
```

**7.2 Frontend Load**
```
URL: https://stock-market-app.onrender.com

Expected: Login page loads (should see form with email/password fields)
```

**7.3 Login Test**
```
Email: test@example.com
Password: password123

Expected: 
- Login succeeds
- Redirects to Dashboard
- Shows "20 stocks" in grid
```

**7.4 Stock Detail Test**
```
1. Click on any stock (e.g., INFY)
2. Expected: Stock detail page loads with:
   - Stock ticker + name
   - Current price
   - 30-day price chart
   - OHLCV data table
```

**7.5 Search Test**
```
1. Dashboard → Search bar
2. Type: "TCS"
3. Expected: Filters to show TCS stock only
4. Type: "" (clear)
5. Expected: Shows all 20 stocks again
```

**Verification Checklist**:
- [ ] Health endpoint responds ✅
- [ ] Frontend loads (no 404)
- [ ] Login works with test credentials
- [ ] Dashboard displays 20 stocks
- [ ] Stock detail shows chart & prices
- [ ] Search filters correctly
- [ ] No console errors (DevTools)

**If any test fails**:
```bash
# Check Render logs for errors:
# Render Dashboard → Logs → search for "ERROR" or "Exception"

# Common fixes:
# 1. Database not seeded - need to SSH in and run seed_data.py
# 2. Frontend build missing - rebuild and push again
# 3. Environment variables wrong - double-check values in Render dashboard
```

---

## Seed Database on Render (SSH)

**Only needed if stocks don't appear after Step 7**

```bash
# 7.6 SSH into Render
# Render Dashboard → Web Service → "Shell" tab

# Once connected:
cd backend
python seed_data.py

# Expected output:
# Seeding database...
# Created test user: test@example.com
# Created 20 stocks with 30 days of price data
# Database seeding complete!

# Then test login again
```

---

## Summary: 7 Steps Complete ✅

| Step | Action | Tool | Duration |
|------|--------|------|----------|
| 1 | Open in VS | VS Code | 1 min |
| 2 | Audit structure | Claude Code | 2 min |
| 3 | Build frontend | npm | 5 min |
| 4 | Verify backend | Claude Code | 2 min |
| 5 | Push to GitHub | git | 2 min |
| 6 | Deploy to Render | Browser | 5 min |
| 7 | Test live app | Browser | 5 min |
| **TOTAL** | **Live on internet** | **Multi** | **~22 min** |

---

## Troubleshooting Quick Reference

| Problem | Cause | Solution |
|---------|-------|----------|
| VS won't open project | VS not installed | `brew install --cask visual-studio-code` |
| npm build fails | Node version too old | `node --version` should be 16+ |
| git push rejected | auth issue | Set up SSH or HTTPS credentials |
| Render build fails | Python version mismatch | Check runtime.txt = python-3.12.3 |
| Stocks don't appear | DB not seeded | SSH in & run seed_data.py |
| Login fails | test user not created | Seed database |
| Search not working | API error | Check Render logs for 500 errors |

---

## What's Next After Live Deployment?

Once Step 7 is complete:

1. **Share URL** - App is live at: `https://stock-market-app.onrender.com`
2. **Monitor** - Check Render dashboard daily for errors
3. **Scale** - If traffic grows, upgrade from Free tier
4. **Enhance** - Add real stock APIs, price alerts, etc.

---

## Command Reference (Copy & Paste)

```bash
# Step 1: Open in VS
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render && code .

# Step 3: Build frontend
cd frontend && npm install && npm run build

# Step 5: Push to GitHub
cd .. && git add . && git commit -m "Build: Frontend ready for Render deployment" && git push origin main

# Step 6: (Browser - render.com dashboard)
# - Create Web Service
# - Create PostgreSQL
# - Set environment variables

# Step 7: Test live (in browser)
# https://stock-market-app.onrender.com
```

---

**Ready to start Step 1?** Open terminal and run the commands above!

Built with ❤️ | Claude Code + Render.com | 2026
