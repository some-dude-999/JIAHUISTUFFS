# Luke Hydro CRM - Backend Setup Guide

## 🚀 Quick Start

### Option 1: Run Locally with Backend (Recommended for Auto-Save)

1. **Install Python dependencies:**
   ```bash
   cd LUKEHYROCRM
   pip install -r requirements.txt
   ```

2. **Start the backend server:**
   ```bash
   python backend.py
   ```

3. **Open the CRM:**
   - Open `LukeHydroCRM.html` in your browser
   - Make sure to use `http://localhost:5000` URL or open the HTML file directly
   - Changes will now automatically save to the CSV!

### Option 2: Run on GitHub Pages (Read-Only)

- Just open the GitHub Pages URL
- Changes are stored in browser localStorage only
- Use Export CSV to download changes

## 🔌 Backend API Endpoints

The Flask backend provides these endpoints:

- `GET /api/contacts` - Get all contacts
- `POST /api/contacts` - Add new contact
- `PUT /api/contacts/:id` - Update contact by index
- `DELETE /api/contacts/:id` - Delete contact by index
- `POST /api/contacts/bulk` - Bulk update all contacts
- `GET /api/health` - Health check

## 📊 How It Works

### With Backend Running:
1. CRM tries to connect to `http://localhost:5000`
2. All changes (add/edit/delete/star) save to CSV immediately
3. Multiple people can use the CRM at the same time

### Without Backend:
1. CRM falls back to localStorage (browser storage)
2. Changes persist in your browser only
3. Use Export CSV to download your data

## 🛠️ Production Deployment Options

### Option A: Deploy on Heroku
```bash
# Create Procfile
echo "web: python backend.py" > Procfile

# Deploy
heroku create your-crm-name
git push heroku main
```

### Option B: Deploy on Railway/Render/Fly.io
- Similar to Heroku, just push the `backend.py` and `requirements.txt`

### Option C: Run on Local Network
```bash
# Start server accessible on local network
python backend.py
# Access from any device on network at: http://YOUR-IP:5000
```

## 📝 Features

- ✅ Real-time CSV read/write
- ✅ Star/favorite contacts
- ✅ Click rows to edit
- ✅ Search and filter
- ✅ Export to CSV
- ✅ Cute emoji rain 🐱🐸🦄🌸
- ✅ Mystical space theme

## 🔒 Security Notes

For production use:
- Add authentication (API keys, JWT, etc.)
- Use HTTPS
- Add rate limiting
- Validate all inputs
- Use a proper database (PostgreSQL, MongoDB, etc.)

## 🐛 Troubleshooting

**Backend won't start:**
```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Check if port 5000 is available
lsof -i :5000  # Kill if something is using it
```

**CRM can't connect to backend:**
- Check if backend is running (`http://localhost:5000/api/health`)
- Check browser console for CORS errors
- Make sure you're using the right backend URL in the HTML

**Changes not saving:**
- Backend must be running
- Check browser console for errors
- Try exporting CSV as backup
