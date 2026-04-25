# Claude Code Integration Guide

Complete guide to use Claude Code in Visual Studio for the Stock Market App deployment.

---

## What is Claude Code?

Claude Code is a **command-line tool** that brings Claude's capabilities directly to your terminal/IDE. It helps you:
- Audit project structure
- Verify code before deployment
- Generate prompts and checklists
- Troubleshoot errors

**It's NOT a replacement for you—it's your assistant.**

---

## Installation & Setup

### Step 1: Install Node.js (if not installed)

**Check if installed**:
```bash
node --version
# Should show: v16.0.0 or higher
```

**If not installed**, download from: https://nodejs.org (LTS version)

### Step 2: Install Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
```

### Step 3: Authenticate Claude Code

```bash
claude-code init
```

This will prompt you for:
- Your Anthropic API key (get from: https://console.anthropic.com/api-keys)
- Workspace directory (use default)

### Step 4: Verify Installation

```bash
claude-code --version
# Should show: 1.x.x or higher
```

---

## How to Use Claude Code in Visual Studio

### Method 1: Claude Code Chat in VS Code Extension

**Install Extension**:
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Claude Code"
4. Click "Install"

**Use in VS**:
1. Open Command Palette (Ctrl+Shift+P)
2. Type "Claude Code: Open Chat"
3. Opens chat panel on right side
4. Paste prompts there

### Method 2: Terminal Commands

**From VS Terminal** (Ctrl+`):

```bash
claude-code audit --project-structure
```

Or paste prompts directly in the chat panel.

---

## 7-Step Deployment Using Claude Code

### Step 1: Open Project
```bash
cd /Users/swapnil/Documents/ClaudeProjects/Market_Analizer/Market_Analizer_render
code .
```

### Step 2: Run Structure Audit
**In Claude Code chat** (use extension panel):

Paste **Prompt 2A** from `CLAUDE_CODE_PROMPTS.md`

**Response**: Should show ✅ for all items

### Step 3: Build Frontend
```bash
# In VS Terminal:
cd frontend
npm install
npm run build
```

**Check**: `frontend/dist/` folder exists with `index.html`

### Step 4: Verify Backend
**In Claude Code chat**:

Paste **Prompt 4A** from `CLAUDE_CODE_PROMPTS.md`

**Response**: Should show ✅ RENDER-READY

### Step 5: Commit & Push
```bash
# In VS Terminal:
git add .
git commit -m "Build: Frontend compiled for production, ready for Render deployment"
git push origin main
```

**Check**: No errors, shows successful push

### Step 6: Deploy to Render
**In browser**: https://dashboard.render.com
- Create Web Service
- Create PostgreSQL
- Set 3 environment variables

**Check**: Status shows "Deployed" (green)

### Step 7: Test Live
**Use Claude Code prompts**:
- Prompt 7A: Health check
- Prompt 7B: Frontend load
- Prompt 7C: Login & dashboard
- Prompt 7D: Stock detail
- Prompt 7E: Search

Or use browser directly to test manually.

---

## Step-by-Step Screenshots (Text Version)

### Opening Claude Code in VS

```
1. VS Code is open with project
2. Press: Ctrl+Shift+P
3. Type: "Claude Code: Open Chat"
4. Chat panel appears on RIGHT side
5. Cursor ready for prompt input
```

### Pasting a Prompt

```
1. Find prompt in CLAUDE_CODE_PROMPTS.md
2. Copy entire prompt (Ctrl+C)
3. Go to Claude Code chat panel
4. Click input field at bottom
5. Paste (Ctrl+V)
6. Press Enter
7. Wait for response
8. Review ✅ or ⚠️ items
```

### Using Terminal in VS

```
1. VS Code window
2. Bottom of screen shows terminal
3. Type commands there (npm, git, etc.)
4. Right panel shows Claude Code chat
5. Switch between them easily
```

---

## Common Claude Code Tasks

### Task: Audit Project Files
```
Prompt: "List all Python files in backend/app/ and report total count"
Response: Shows file list and count
Use: Verify no files are missing
```

### Task: Verify Build Success
```
Prompt: "Check if frontend/dist/ has index.html and assets with .js and .css files"
Response: Confirms build or lists missing files
Use: Before pushing to GitHub
```

### Task: Check Environment Variables
```
Prompt: "Validate these environment variable formats:
- JWT_SECRET_KEY: base64 string (43 chars)
- DATABASE_URL: postgresql://user:pass@host:5432/db
- FLASK_ENV: production"
Response: Shows if format is correct
Use: Before setting in Render
```

### Task: Troubleshoot Error
```
Prompt: "I got this error: [paste error message]. What does it mean and how do I fix it?"
Response: Explains error and provides fix steps
Use: When something breaks
```

---

## Pro Tips for Using Claude Code

### Tip 1: Be Specific
✅ Good:
```
"Verify backend/app/models/ has exactly 7 files: user.py, stock.py, price.py, portfolio.py, holding.py, watchlist.py, watchlist_item.py"
```

❌ Bad:
```
"Check if models folder is OK"
```

### Tip 2: Provide Context
✅ Good:
```
"I'm deploying to Render.com (Python 3.12.3). Check if requirements.txt has gunicorn 21.2.0"
```

❌ Bad:
```
"Is gunicorn in requirements.txt?"
```

### Tip 3: Ask for Format
✅ Good:
```
"Report in checklist format: ✅ if correct, ⚠️ if issue"
```

❌ Bad:
```
"Check it"
```

### Tip 4: Break Down Large Requests
✅ Good:
```
"Task 1: Count files in backend/app/models/ (should be 7)
Task 2: Count files in backend/app/routes/ (should be 5)
Task 3: Verify requirements.txt has Flask, SQLAlchemy, gunicorn"
```

❌ Bad:
```
"Check everything"
```

### Tip 5: Use Copy/Paste Ready Prompts
✅ Good:
Use pre-written prompts from `CLAUDE_CODE_PROMPTS.md`

❌ Bad:
Try to write your own prompts from scratch

---

## Integration with VS Code

### Keyboard Shortcuts
- **Ctrl+Shift+P** - Open Command Palette
- **Ctrl+`** - Toggle Terminal
- **Ctrl+J** - Toggle Panel (includes Claude Code chat)

### Layout Tips
```
┌─────────────────────────────────┐
│         File Explorer           │
│      (left sidebar)             │
├──────────────┬──────────────────┤
│              │   Editor View    │
│   File Tree  │   (your code)    │
│              │                  │
├──────────────┼──────────────────┤
│    Claude Code Chat Panel (right) │
│                                  │
└──────────────────────────────────┘
```

### Recommended Workflow
1. **Left**: File tree (shows project structure)
2. **Center**: Editor (modify code if needed)
3. **Bottom**: Terminal (run commands)
4. **Right**: Claude Code chat (paste prompts, get responses)

---

## Troubleshooting Claude Code Issues

### Issue: "Command not found: claude-code"
```bash
# Fix 1: Reinstall
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code

# Fix 2: Use npx instead
npx claude-code --version
```

### Issue: "Authentication failed"
```bash
# Fix: Re-authenticate
claude-code init

# Then paste your API key when prompted
# Get key from: https://console.anthropic.com/api-keys
```

### Issue: Claude Code chat not showing in VS
```bash
# Fix 1: Restart VS Code

# Fix 2: Reinstall extension
# Extensions → Search "Claude Code" → Install

# Fix 3: Open command palette
Ctrl+Shift+P → "Claude Code: Open Chat"
```

---

## File References

When using Claude Code, reference these files in your prompts:

| File | Purpose |
|------|---------|
| `CLAUDE_CODE_WORKFLOW.md` | Detailed 7-step guide |
| `CLAUDE_CODE_PROMPTS.md` | Copy/paste prompts for Claude Code |
| `QUICK_START_CARD.md` | Quick reference card |
| `DEPLOYMENT_CHECKLIST.md` | Checklist to mark off progress |
| `README.md` | Project overview |
| `DEPLOYMENT_GUIDE.md` | Render.com deployment details |
| `ARCHITECTURE.md` | Technical architecture |

---

## Example: Complete Step 2 Using Claude Code

**What you do**:
1. Open VS Code with project
2. Press Ctrl+Shift+P
3. Type "Claude Code: Open Chat"
4. Open `CLAUDE_CODE_PROMPTS.md` (in same VS window)
5. Find "Prompt 2A: Full Structure Audit"
6. Copy entire prompt (Ctrl+C)
7. Go to Claude Code chat panel (right side)
8. Paste prompt (Ctrl+V)
9. Press Enter

**What Claude Code does**:
- Scans your project structure
- Checks for 7 models, 5 routes
- Verifies dependencies
- Reports ✅ or ⚠️ for each item

**What you do next**:
- If all ✅: proceed to Step 3
- If any ⚠️: fix issue, then repeat Step 2

---

## Quick Command Reference

```bash
# Check installation
claude-code --version

# Authenticate
claude-code init

# Run audits
claude-code audit --project-structure

# Manual commands in VS Terminal
cd /path/to/project
npm run build
git push origin main
```

---

## When to Use vs. When to Skip Claude Code

### ✅ USE Claude Code for:
- Auditing project structure before deployment
- Verifying dependencies match requirements
- Checking file formats and content
- Troubleshooting errors
- Validating configurations

### ⏭️ SKIP Claude Code for:
- Running npm/git commands (use terminal directly)
- Editing code (use VS editor directly)
- Deploying to Render (use browser dashboard)
- Manual testing (use browser directly)

---

## Summary

**Claude Code is your deployment assistant:**

1. ✅ Use it to verify each step
2. ✅ Copy/paste pre-written prompts
3. ✅ Review responses for ✅ or ⚠️
4. ⏭️ Follow terminal commands separately
5. ⏭️ Proceed to next step when ready

**Total setup**: 5 minutes
**Per-deployment usage**: ~15 minutes

---

## Next Steps

1. **Install Claude Code** (follow steps above)
2. **Open VS with project** (`code .`)
3. **Start Step 1** of `CLAUDE_CODE_WORKFLOW.md`
4. **Use Prompt 2A** from `CLAUDE_CODE_PROMPTS.md`
5. **Follow checklist** in `DEPLOYMENT_CHECKLIST.md`

---

**Ready?** Start with installation steps above! 🚀

Built with ❤️ | Claude Code | 2026
