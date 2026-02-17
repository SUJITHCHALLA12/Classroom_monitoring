# 🚀 Deployment Guide - Make Your App Online

This guide will help you deploy your Classroom & Timetable Monitoring System to the internet.

---

## ⚡ Quick Deployment Options (Easiest First)

### Option 1: Render (Recommended - Free & Easy)

**Best for:** Beginners, quick deployment, free tier available

#### Steps:

1. **Create Render Account**
   - Go to https://render.com
   - Sign up (free)

2. **Push Code to GitHub**
   ```powershell
   # If not already a git repo
   git init
   git add .
   git commit -m "Initial commit"
   ```
   - Create a GitHub account if needed
   - Create a new repository
   - Push your code: `git push -u origin main`

3. **Deploy on Render**
   - Go to https://render.com/dashboard
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name:** classroom-timetable
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Free Plan:** Yes
   - Click "Deploy"

4. **Your app will be live at:** `https://classroom-timetable.onrender.com`

---

### Option 2: Heroku (Free with limitations)

**Best for:** Reliable hosting, but free tier ending

#### Steps:

1. **Install Heroku CLI**
   - Download from https://devcenter.heroku.com/articles/heroku-cli
   - Install and login: `heroku login`

2. **Create Heroku App**
   ```powershell
   heroku create my-classroom-app
   git push heroku main
   ```

3. **Your app will be live at:** `https://my-classroom-app.herokuapp.com`

---

### Option 3: PythonAnywhere (Easy, Free Tier)

**Best for:** Simple deployments, easy to manage

#### Steps:

1. **Create Account**
   - Go to https://www.pythonanywhere.com
   - Sign up (free tier available)

2. **Upload Code**
   - Use WebTab or upload files via the web interface
   - Create a new web app

3. **Configure**
   - Set WSGI configuration to point to `app:app`
   - Reload web app

4. **Your app will be live at:** `https://yourusername.pythonanywhere.com`

---

## 🌐 Domain Setup (Optional)

Once deployed, you can add a custom domain:

1. **Buy a domain** from:
   - Godaddy.com
   - Namecheap.com
   - Google Domains

2. **Configure DNS** to point to your hosting platform

3. **Set custom domain** in your platform's settings

---

## 📝 Environment Variables

Set these variables in your hosting platform:

```
SECRET_KEY=your-random-secret-key-here
FLASK_ENV=production
DATABASE_URL=your-database-url (if using PostgreSQL)
```

---

## 🗄️ Database Considerations

### Current Setup (SQLite)
- Works on all platforms
- Good for small apps
- Data reset on some platforms with ephemeral storage

### Production Setup (PostgreSQL) - Recommended
- More reliable
- Better for larger apps
- Free tier available on most platforms

#### To upgrade to PostgreSQL:

1. **Update requirements.txt:**
   ```
   Flask==3.0.0
   Flask-SQLAlchemy==3.1.1
   SQLAlchemy==2.0.23
   Werkzeug==3.0.1
   gunicorn==21.2.0
   psycopg2-binary==2.9.9
   ```

2. **Update app.py database config:**
   ```python
   import os
   database_url = os.environ.get('DATABASE_URL', 'sqlite:///classroom_timetable.db')
   if database_url.startswith('postgres://'):
       database_url = database_url.replace('postgres://', 'postgresql://', 1)
   app.config['SQLALCHEMY_DATABASE_URI'] = database_url
   ```

3. **Get database URL from your hosting provider** and set as environment variable

---

## 🔐 Security Checklist

- [ ] Change `SECRET_KEY` to a random string
- [ ] Set `FLASK_ENV=production`
- [ ] Disable debug mode in production
- [ ] Use HTTPS (automatically provided by Render/Heroku)
- [ ] Set strong SECRET_KEY in environment variables
- [ ] Consider adding authentication for admin features

---

## ✅ Verification

After deployment, verify:

1. **Homepage loads:** Visit your app URL
2. **Dashboard displays:** Check all statistics load
3. **Create resources:** Try adding a classroom
4. **Database works:** Data persists after page refresh

---

## 🆘 Troubleshooting

### App won't start
```
Check logs on your hosting platform for error messages
Usually shows in the "Logs" section of your dashboard
```

### Port issues
```
This is automatically handled by the hosting platform
The environment variable PORT is used
```

### Database errors
```
Try recreating the database by redeploying
Or use the Models to create tables on startup
```

### Cold starts
```
Free tier apps may take 50 seconds to start
This is normal - just wait for the app to wake up
```

---

## 📊 Accessing Your Live App

After deployment:

| Component | URL |
|-----------|-----|
| Dashboard | `https://your-app-url.com` |
| Classrooms | `https://your-app-url.com/classrooms` |
| Teachers | `https://your-app-url.com/teachers` |
| Students | `https://your-app-url.com/students` |
| Timetables | `https://your-app-url.com/timetables` |
| API | `https://your-app-url.com/api/*` |

---

## 📚 Resources

- [Render Deployment Guide](https://render.com/docs)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [PythonAnywhere Docs](https://help.pythonanywhere.com/)
- [Flask Deployment](https://flask.palletsprojects.com/deployment/)

---

## 🎯 Next Steps

1. Choose a deployment option above
2. Follow the steps for your chosen platform
3. Share your live app URL with teachers and students
4. Load sample data via `/api` or UI
5. Start using the system online!

---

**Your app is production-ready and can handle real classroom data!** 🎓✨
