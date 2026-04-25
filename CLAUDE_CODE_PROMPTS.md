# Claude Code - Copy/Paste Prompts for Each Step

Ready-to-use prompts for Claude Code throughout the 7-step deployment process.

---

## STEP 2: Project Structure Audit

**When**: After Step 1 (project open in VS)

**How to use**:
1. Open Claude Code in VS (Command Palette: "Claude Code: Open")
2. Copy prompt below
3. Paste into Claude Code chat
4. Wait for response

---

### Prompt 2A: Full Structure Audit

```
PROJECT STRUCTURE AUDIT

I have a Stock Market Analysis app ready for Render.com deployment.

Base directory: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render

Please audit the following and report ONLY findings (do NOT modify anything):

BACKEND STRUCTURE CHECK:
1. backend/app/models/ directory
   - Should contain exactly 7 Python files:
     ✓ user.py
     ✓ stock.py
     ✓ price.py
     ✓ portfolio.py
     ✓ holding.py
     ✓ watchlist.py
     ✓ watchlist_item.py
   - Report: Found X/7 files

2. backend/app/routes/ directory
   - Should contain exactly 5 Python files:
     ✓ health.py
     ✓ auth.py
     ✓ stocks.py
     ✓ portfolio.py
     ✓ watchlist.py
   - Report: Found X/5 files

3. backend/ root files
   - app/__init__.py → Should have create_app() function
   - app/config.py → Should handle DATABASE_URL and JWT_SECRET_KEY from environment
   - run.py → Should read PORT from environment
   - seed_data.py → Should create 20 stocks + 1 user + 600 price records
   - requirements.txt → Should have these exact packages:
     * Flask==2.3.3
     * SQLAlchemy==2.0.35
     * Flask-JWT-Extended==4.5.2
     * Flask-CORS==4.0.0
     * psycopg2-binary==2.9.7
     * Werkzeug==2.3.7
     * python-dotenv==1.0.0
     * gunicorn==21.2.0
   - Procfile → Should contain: web: gunicorn "app:create_app()"
   - runtime.txt → Should contain: python-3.12.3

FRONTEND STRUCTURE CHECK:
1. frontend/package.json
   - Should list these dependencies:
     * react 18.2.0+
     * vite 4.4.5+
     * axios 1.4.0+
     * chart.js 3.9.1+

2. frontend/src/pages/
   - Should have 5 JSX files: Login, Dashboard, StockDetail, Portfolio, Watchlist

3. frontend/src/components/
   - Should have 5 JSX files: NavBar, StockCard, SearchBar, PriceChart, (plus CSS)

4. frontend/.env
   - Should have: VITE_API_URL=http://localhost:5001

DOCUMENTATION CHECK:
1. Root directory should have:
   - README.md
   - LOCAL_SETUP.md
   - DEPLOYMENT_GUIDE.md
   - ARCHITECTURE.md
   - PROJECT_SUMMARY.md
   - CLAUDE_CODE_WORKFLOW.md
   - .gitignore

OUTPUT FORMAT:
Report each section with:
✅ if all items present and correct
⚠️ if some items missing (list which ones)
❌ if critical items missing

Do NOT suggest fixes, only report findings.
```

---

## STEP 3: Frontend Build Verification

**When**: After `npm run build` completes

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit
4. Verify output

---

### Prompt 3A: Verify Production Build

```
FRONTEND BUILD VERIFICATION

I just ran: npm run build

Please verify the production build was successful.

Check these files/directories exist:

1. frontend/dist/ directory
   - Should exist and be a folder (not empty)

2. frontend/dist/index.html
   - Should exist
   - Should be ≥ 1 KB in size
   - Should NOT contain webpack or vite dev code

3. frontend/dist/assets/ directory
   - Should contain at least 2 files:
     * One .js file (main bundle, should be ≥ 50 KB)
     * One .css file (should be ≥ 10 KB)
   - File names should have hash: like index-XXXXX.js (where XXXXX is hash)

4. NO development artifacts
   - Should NOT have .map files (if minified correctly)
   - Should NOT have node_modules in dist/

REPORT FORMAT:
✅ Build successful - all checks passed
or
❌ Build failed - these items missing: [list items]

If build failed, suggest re-running: rm -rf dist && npm run build
```

---

## STEP 4: Backend Render Readiness Check

**When**: Before pushing to GitHub

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit
4. Verify ✅ for each item

---

### Prompt 4A: Render Deployment Checklist

```
BACKEND RENDER.COM READINESS CHECK

I'm preparing to deploy to Render.com (Python 3.12.3)

Base: /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render/backend

Verify these critical files for Render compatibility:

1. runtime.txt
   Contents should be EXACTLY: python-3.12.3
   (nothing else, no spaces)

2. Procfile
   Contents should be EXACTLY: web: gunicorn "app:create_app()"
   (this is how Render starts the app)

3. requirements.txt
   Should contain (exact versions):
   ✓ Flask==2.3.3
   ✓ Flask-SQLAlchemy==3.0.5
   ✓ Flask-JWT-Extended==4.5.2
   ✓ Flask-CORS==4.0.0
   ✓ psycopg2-binary==2.9.7
   ✓ SQLAlchemy==2.0.35
   ✓ Werkzeug==2.3.7
   ✓ python-dotenv==1.0.0
   ✓ gunicorn==21.2.0

4. app/__init__.py
   Should have:
   ✓ def create_app(): function
   ✓ Initializes SQLAlchemy, JWT, CORS
   ✓ Registers blueprints
   ✓ Serves React frontend from dist/

5. app/config.py
   Should have:
   ✓ Reads DATABASE_URL from environment (handles postgres:// → postgresql://)
   ✓ Reads JWT_SECRET_KEY from environment
   ✓ SQLALCHEMY_TRACK_MODIFICATIONS = False

6. run.py
   Should have:
   ✓ Reads PORT from environment (default 5001)
   ✓ Creates app using create_app()
   ✓ Runs with: app.run(debug=False, host='0.0.0.0', port=port)

REPORT FORMAT:
For each item above (1-6):
✅ Verified - correct format/content
⚠️ Minor issue - [describe]
❌ Problem - [describe]

At end, report:
✅ RENDER-READY if all pass
or
⚠️ NEEDS FIXES - fix before Step 5

Do NOT modify any files, only report.
```

---

## STEP 5: Git Commit Verification

**When**: Before `git push`

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit
4. Verify safe to push

---

### Prompt 5A: Pre-Push Safety Check

```
GIT COMMIT SAFETY CHECK

I'm about to push to GitHub.

Verify these before I push:

1. frontend/dist/ folder
   - Should be staged for commit (will include compiled JS/CSS)
   - Should NOT be in .gitignore (it needs to go to GitHub)

2. No sensitive files being committed
   - Should NOT include: .env (only .env.example)
   - Should NOT include: database files
   - Should NOT include: node_modules/
   - Should NOT include: __pycache__/
   - Should NOT include: .pyc files

3. backend/requirements.txt
   - Should be staged
   - Should have frozen versions (not "*")

4. All documentation files
   - README.md, DEPLOYMENT_GUIDE.md, etc. should be staged

5. .gitignore
   - Should exist and contain standard patterns

REPORT FORMAT:
✅ Safe to push - all checks passed
or
⚠️ Warning - these files might cause issues: [list]
or
❌ DO NOT PUSH - fix these first: [list]

After fix, run: git add . && git commit -m "..." && git push origin main
```

---

## STEP 6: Environment Variable Validation

**When**: After setting env vars in Render dashboard

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit
4. Verify correct format

---

### Prompt 6A: Environment Variable Format Check

```
RENDER.COM ENVIRONMENT VARIABLES FORMAT CHECK

I'm about to set these environment variables in Render dashboard.

Please verify the format and values are correct:

VARIABLE 1:
KEY: JWT_SECRET_KEY
VALUE: (should be output of: python3 -c "import secrets; print(secrets.token_urlsafe(32))")
Expected format: 43-character base64 string (like: "AbCdEfGhIjKlMnOpQrStUvWxYz12345678901234")

VARIABLE 2:
KEY: FLASK_ENV
VALUE: production
Expected: exactly "production" (lowercase)

VARIABLE 3:
KEY: DATABASE_URL
VALUE: postgresql://postgres:PASSWORD@HOSTNAME:5432/stock_db
Expected format: postgresql:// (NOT postgres://)
              - Contains user:password@hostname:5432/database

REPORT FORMAT:
For each variable:
✅ Format correct - ready to paste into Render
⚠️ Format issue - [describe fix]
❌ Value missing - [describe what to do]

Safety check:
⚠️ Warn if DATABASE_URL contains postgres:// (must be postgresql://)
⚠️ Warn if FLASK_ENV not exactly "production"
```

---

## STEP 7A: Health Endpoint Test

**When**: After deployment succeeds on Render

**How to use**:
1. Get your Render URL: https://stock-market-app.onrender.com
2. Open Claude Code
3. Copy prompt below
4. Paste (replace YOUR_RENDER_URL)
5. Submit

---

### Prompt 7A: Verify Health Endpoint

```
TEST HEALTH ENDPOINT

I deployed to Render at: https://YOUR_RENDER_URL

Test if the backend is running by checking the health endpoint.

Expected test:
GET request to: https://YOUR_RENDER_URL/health

Expected response:
Status: 200 OK
Body: {"status": "healthy", "message": "Stock Market API is running"}

Please provide:
1. Test instructions (exact URL to visit or curl command)
2. Expected response format
3. What to check if response fails (404, 500, timeout)
4. Troubleshooting steps if health check fails

Provide in clear, step-by-step format.
```

---

## STEP 7B: Frontend Load Test

**When**: After health check passes

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste (replace YOUR_RENDER_URL)
4. Submit

---

### Prompt 7B: Verify Frontend Loads

```
TEST FRONTEND LOAD

I deployed to Render at: https://YOUR_RENDER_URL

Test if the React frontend loads correctly.

Expected test:
1. Open browser
2. Go to: https://YOUR_RENDER_URL
3. Should see login page with email/password form

Please provide:
1. Exact URL to visit
2. What should appear on screen (login form with fields)
3. Check browser DevTools Console for errors
   - Should have NO red errors
   - May have warnings (OK)

If page is blank or shows error:
- Check: frontend/dist/index.html was built
- Check: backend is serving static files correctly
- Check: Render logs for 404 or 500 errors

Provide troubleshooting in order of likelihood.
```

---

## STEP 7C: Login & Dashboard Test

**When**: After frontend loads

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit

---

### Prompt 7C: Test Login & Dashboard

```
TEST LOGIN & DASHBOARD

Frontend is now loaded at: https://YOUR_RENDER_URL

Test the login functionality:

Step-by-step test:
1. See login form with 2 fields: email, password
2. Enter:
   Email: test@example.com
   Password: password123
3. Click Login button
4. Expected: Page redirects to /dashboard
5. Expected: See grid of stock cards (should be 20 stocks)
6. Each card should show: ticker, name, current price

STOCK CARDS should display:
- Ticker (e.g., INFY, TCS, WIPRO)
- Company name (e.g., Infosys Limited)
- Price in ₹ (e.g., ₹1,096.00)
- "View Details" button

If login fails:
- Check API endpoint: /auth/login
- Verify database was seeded with test user
- Check Render logs for authentication error

If dashboard blank:
- Stocks API endpoint: /stocks
- Check Render logs for database connection error
- Verify PostgreSQL is seeded with 20 stocks

Provide troubleshooting checklist.
```

---

## STEP 7D: Stock Detail & Chart Test

**When**: After dashboard displays stocks

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit

---

### Prompt 7D: Test Stock Detail Page

```
TEST STOCK DETAIL PAGE

Dashboard is showing 20 stocks.

Test stock detail page:

Step-by-step test:
1. On dashboard, click any stock card (e.g., INFY)
2. Should navigate to: /stock/INFY
3. Page should display:
   ✓ Stock ticker: INFY
   ✓ Stock name: Infosys Limited
   ✓ Exchange: NSE
   ✓ Current price: ₹1,096.00 (or current price)
   ✓ Price chart (30-day line chart)
   ✓ OHLCV data table with columns:
     - Date
     - Open
     - High
     - Low
     - Close
     - Volume

CHART should:
- Show 30 days of data
- Display line going up/down
- Have tooltip on hover
- Have legend at top

TABLE should:
- Show 30 rows (one per day)
- Prices in ₹ currency
- Volume in millions (e.g., 5.00M)

If chart not visible:
- Check Chart.js loaded (DevTools Network tab)
- Check API endpoint: /stocks/INFY/prices
- Verify prices in database (should be 30 records)

If table empty:
- Verify seed_data.py created price records
- Check Render logs for database errors

Provide verification steps and troubleshooting.
```

---

## STEP 7E: Search Functionality Test

**When**: After stock detail works

**How to use**:
1. Open Claude Code
2. Copy prompt below
3. Paste and submit

---

### Prompt 7E: Test Search Feature

```
TEST SEARCH FUNCTIONALITY

Stock detail page is working.

Test search on dashboard:

Step-by-step test:
1. Go back to dashboard (click logo or "Dashboard" in nav)
2. See search bar at top: "Search by ticker or name..."
3. Type: TCS
   - Expected: Grid updates to show only TCS stock
   - Should filter in real-time (no refresh needed)
4. Type: Wipro
   - Expected: Shows only WIPRO stock
5. Delete search text (clear field)
   - Expected: Shows all 20 stocks again
6. Type: INVALID
   - Expected: Shows "No stocks found" message

SEARCH should:
- Work by ticker (INFY, TCS, WIPRO)
- Work by partial name (Infosys, Tata, Wipro)
- Be case-insensitive (infy = INFY)
- Update results without page reload (debounced)
- Show "No data" if no matches

If search not working:
- Check search API: GET /stocks?search=INFY
- Verify backend search is case-insensitive
- Check browser DevTools for API errors

If slow to respond:
- Search should be debounced (wait 300ms before API call)
- Check Render logs for slow queries

Provide verification checklist.
```

---

## EMERGENCY: App Not Working

**If any step fails, use this prompt:**

---

### Prompt EMERGENCY: Troubleshooting Guide

```
EMERGENCY TROUBLESHOOTING

My Stock Market app on Render isn't working.

Symptom: [describe what's happening]

Please provide:

1. DIAGNOSTIC STEPS (what to check first)
   - URL to visit
   - API endpoint to test
   - Browser console check
   - Render logs to examine

2. LIKELY CAUSES (in order of probability)
   - Most common issues for this symptom
   - What to look for in logs

3. FIXES (step-by-step)
   - Quick fixes first
   - Then deeper troubleshooting
   - Then rebuild/redeploy if needed

4. VERIFICATION
   - How to confirm it's fixed
   - Test to run after each fix

Format as actionable checklist, not explanation.
```

---

## Summary: Which Prompt to Use When

| Step | Prompt | When to Use |
|------|--------|------------|
| 2 | 2A | After opening project in VS |
| 3 | 3A | After `npm run build` completes |
| 4 | 4A | Before `git push` |
| 5 | 5A | Before `git commit` |
| 6 | 6A | When setting Render env vars |
| 7A | 7A | After Render shows "Deployed" |
| 7B | 7B | After health endpoint works |
| 7C | 7C | After frontend loads |
| 7D | 7D | After login works |
| 7E | 7E | After stock detail works |
| Emergency | EMERGENCY | If anything breaks |

---

**Ready?** Start with **Prompt 2A** and follow the checklist!

Built with ❤️ | Claude Code | 2026
