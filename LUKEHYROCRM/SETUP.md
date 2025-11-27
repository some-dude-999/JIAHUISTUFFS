# Luke Hydro CRM - GitHub Auto-Save Setup

## 🚀 Quick Setup (One-Time, 2 Minutes)

Your CRM now saves **directly to GitHub** - no local server needed!

### Step 1: Create a GitHub Token

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name: `Luke Hydro CRM`
4. Select scope: **`repo`** (check the box)
5. Click **"Generate token"** at bottom
6. **COPY THE TOKEN** (you won't see it again!)

### Step 2: Add Token to CRM

1. Open your CRM: https://some-dude-999.github.io/JIAHUISTUFFS/LUKEHYROCRM/LukeHydroCRM.html
2. Click **"🔐 Setup GitHub Auto-Save"** button
3. Paste your token
4. Click OK

**Done!** ✅ All changes now auto-save to GitHub!

---

## How It Works

### With GitHub Token (Recommended):
- ✅ Changes save directly to `LukeHydroCRM.csv` in your repo
- ✅ Creates automatic commits
- ✅ Works from any device
- ✅ Team members can share data
- ✅ Full version history in GitHub

### Without Token:
- ⚠️ Changes save to browser only (localStorage)
- ⚠️ Not shared between devices
- ⚠️ Must export CSV manually

---

## Features

- **Star/Favorite Contacts** - Mark important leads
- **Auto-Save** - Every change commits to GitHub
- **Search** - Real-time filtering
- **Sort** - Click column headers
- **Click-to-Edit** - Click any row to edit
- **Export CSV** - Download backup anytime
- **Emoji Rain** - Cute cats, frogs, unicorns 🐱🐸🦄

---

## Security

- Token is stored in browser localStorage only
- Never committed to repo
- Only you can see it
- Can be removed anytime with `removeGitHubToken()` in console

---

## Troubleshooting

**"Failed to save to GitHub":**
- Check if token is valid
- Make sure token has `repo` scope
- Try removing and re-adding token

**"No data showing":**
- Refresh the page
- Check browser console for errors
- Try clicking "📥 Reload Data"

**"Want to remove token":**
- Open browser console (F12)
- Type: `removeGitHubToken()`
- Press Enter
