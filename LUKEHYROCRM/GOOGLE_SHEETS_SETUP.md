# Google Sheets Auto-Save Setup (NO TOKEN NEEDED!)

## 🎯 This is MUCH better than GitHub!

✅ **No tokens for users**
✅ **Anyone can edit and save**
✅ **Real-time sync**
✅ **Everyone sees same data**
✅ **5 minute setup**

---

## 📋 Setup Steps

### Step 1: Open Your Google Sheet

1. Go to: https://sheets.google.com
2. Open your existing sheet OR create a new one
3. Make sure it has this structure:

| Date Contacted | PIC | Business | Number | Location | Attempts | Notes | Probability | Email | Business Type | Starred |
|----------------|-----|----------|--------|----------|----------|-------|-------------|-------|---------------|---------|

### Step 2: Add Apps Script

1. In your Google Sheet, click **Extensions** → **Apps Script**
2. Delete any existing code in the editor
3. Copy ALL the code from `GoogleSheetScript.js`
4. Paste it into the Apps Script editor
5. (Optional) Change `SHEET_NAME` if your tab isn't called "Sheet1"

### Step 3: Deploy as Web App

1. Click **Deploy** → **New deployment**
2. Click the gear icon ⚙️ → Select **Web app**
3. Fill in:
   - **Description:** Luke Hydro CRM Backend
   - **Execute as:** **Me** (your email)
   - **Who has access:** **Anyone**
4. Click **Deploy**
5. Click **Authorize access**
6. Choose your Google account
7. Click **Advanced** → **Go to [project name] (unsafe)** → **Allow**
8. **COPY THE WEB APP URL** (looks like: https://script.google.com/macros/s/ABC123.../exec)

### Step 4: Update Your CRM

1. Open `LUKEHYROCRM/LukeHydroCRM.html`
2. Find line ~665 (the configuration section)
3. Replace the GitHub configuration with:

```javascript
// Google Sheets Configuration
const APPS_SCRIPT_URL = 'PASTE_YOUR_WEB_APP_URL_HERE';
const USE_GOOGLE_SHEETS = true;
```

4. Save and push to GitHub

---

## 🎉 Done!

Now when ANYONE visits:
- https://some-dude-999.github.io/JIAHUISTUFFS/LUKEHYROCRM/LukeHydroCRM.html

They can:
- ✅ View all contacts
- ✅ Add/Edit/Delete contacts
- ✅ Star favorites
- ✅ All changes save to YOUR Google Sheet
- ✅ **NO TOKEN NEEDED!**

---

## 🔐 Security

**Q: Can anyone edit my sheet?**
A: Only through the CRM. They can't access your sheet directly.

**Q: What if I want to restrict access?**
A: In the Deploy settings, change "Anyone" to "Anyone with Google account" and users will need to sign in with Google.

**Q: Can I see who made changes?**
A: Not by default, but you can add a "Last Modified By" column in the script if needed.

---

## 🛠️ Troubleshooting

**"Script not authorized":**
- Make sure you clicked "Allow" when authorizing
- Try re-deploying with a new deployment

**"Sheet not found":**
- Check the `SHEET_NAME` variable matches your tab name
- Tab names are case-sensitive!

**"CORS error":**
- Make sure you deployed as a "Web app" not "API executable"
- Make sure "Who has access" is set to "Anyone"

---

## 💡 Pro Tips

1. **Sheet Structure:** Don't change column order - the script expects this exact order
2. **Multiple Sheets:** Want separate CRMs? Deploy different web apps for different sheets
3. **Backup:** Google Sheets auto-saves version history (File → Version history)
4. **Import Existing Data:** Just paste your CSV data into the Google Sheet

---

## 🔄 Migration from CSV

If you have data in `LukeHydroCRM.csv`:

1. Open your Google Sheet
2. File → Import → Upload
3. Select your CSV file
4. Import it
5. Done! All your data is now in Google Sheets
