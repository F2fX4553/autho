# SIBNA - Deployment Guide for Claw.cloud

## 📁 Structure

```
Deploy/
├── backend/     ← Upload this as a Docker app on claw.cloud
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env.example   ← Set your real values in the claw.cloud dashboard
│   └── .dockerignore
│
└── frontend/    ← Update the API URL here, then run on your device
    └── (copy your sibna_app Flutter project here)
```

---

## 🚀 BACKEND DEPLOYMENT (claw.cloud) — Step by Step

### Step 1 — Prepare your GitHub Repository
1. Create a **new repository** on GitHub (e.g. `sibna-backend-prod`)
2. Upload **only** the contents of the `Deploy/backend/` folder to the root of the repo
3. Make sure `.env` is **NOT** in the repository (it's in `.dockerignore`)

### Step 2 — Create a PostgreSQL Database on claw.cloud
1. Log in to `eu-central-1.run.claw.cloud`
2. Click **"New"** → **"Database"** → Choose **PostgreSQL**
3. Note down the connection credentials:
   - **Host**, **Port**, **Username**, **Password**, **Database name**
4. Your `DATABASE_URL` will be in this format:
   ```
   postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME
   ```

### Step 3 — Deploy the Backend
1. On claw.cloud, click **"New"** → **"App"** → **"Deploy from GitHub"**
2. Connect your GitHub account and select your `sibna-backend-prod` repo
3. claw.cloud will automatically detect the `Dockerfile`

### Step 4 — Set Environment Variables (IMPORTANT ⚠️)
In the claw.cloud dashboard for your app, go to **"Environment Variables"** and add:

| Variable | Value |
|---|---|
| `SECRET_KEY` | Run `python -c "import secrets; print(secrets.token_hex(32))"` and paste result |
| `JWT_SECRET` | Run same command again for a different key |
| `GMAIL_USER` | `your-email@gmail.com` |
| `GMAIL_APP_PASSWORD` | Your 16-char Google App Password |
| `DATABASE_URL` | `postgresql://user:pass@host:port/db` (from Step 2) |
| `OTP_EXPIRY` | `120` |
| `JWT_EXPIRY_DAYS` | `30` |
| `ENVIRONMENT` | `production` |

### Step 5 — Note your Backend URL
After deployment, claw.cloud will give you a URL like:
```
https://your-app-name.eu-central-1.run.claw.cloud
```
**Copy this URL — you'll need it for the Flutter app.**

---

## 📱 FRONTEND (Flutter App) — What to Change

1. Open `frontend/lib/core/constants/constants.dart`
2. Replace the `baseUrl` with your claw.cloud backend URL:
   ```dart
   // BEFORE (local development)
   static const String baseUrl = 'http://192.168.1.x:8000';
   
   // AFTER (production)
   static const String baseUrl = 'https://your-app-name.eu-central-1.run.claw.cloud';
   ```
3. Run `flutter run` or build a release APK with `flutter build apk`

---

## ✅ Test your deployment

Check the backend is live by visiting:
```
https://your-app-name.eu-central-1.run.claw.cloud/health
```
You should see: `{"status": "healthy", ...}`

The API docs are available at:
```
https://your-app-name.eu-central-1.run.claw.cloud/docs
```
