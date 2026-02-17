# 🚀 Deploy to Render in 3 Steps

Git is not installed yet. Here's the complete setup:

## Step 1: Install Git (5 minutes)

1. **Download Git:**
   - Go to https://git-scm.com/download/win
   - Click download for Windows
   - Run the installer
   - Use default settings
   - Restart your terminal after installation

2. **Verify installation:**
   ```powershell
   git --version
   ```

## Step 2: Create GitHub Repository (5 minutes)

1. **Create GitHub account** (if you don't have one)
   - Go to https://github.com/signup
   - Sign up with email, password, username
   - Verify your email

2. **Create a new repository:**
   - Go to https://github.com/new
   - Name: `classroom-timetable`
   - Description: "Classroom & Timetable Monitoring System"
   - Make it **Public**
   - Click "Create repository"

3. **Initial Git setup** (save these commands):
   ```powershell
   cd "C:\Users\rohith\ClassroomTimetable"
   
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   
   git init
   git add .
   git commit -m "Initial commit: Classroom Timetable app ready for deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/classroom-timetable.git
   git push -u origin main
   ```
   
   **Replace `YOUR_USERNAME`** with your actual GitHub username!

## Step 3: Deploy to Render (2 minutes)

1. **Create Render account:**
   - Go to https://render.com
   - Sign up (use GitHub account for easy login)

2. **Connect your GitHub repo:**
   - Dashboard → "New +" → "Web Service"
   - Select "Connect Repository"
   - Choose `classroom-timetable`
   - Authorize Render to access GitHub

3. **Configure deployment:**
   - **Name:** `classroom-timetable`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Your app will be at: `https://classroom-timetable.onrender.com`

---

## ✅ You're Live!

Once deployed:
- Visit `https://classroom-timetable.onrender.com`
- Share the link with anyone
- They can access your app from anywhere

## 🔄 Making Changes

After deployment, to update your app:

```powershell
# 1. Make changes to your files
# 2. Commit and push to GitHub
git add .
git commit -m "Description of changes"
git push

# 3. Render auto-deploys within 1-2 minutes!
```

---

## 🆘 Need Help?

**Git not working?**
- Restart PowerShell after installing Git
- Try: `git --version`

**GitHub auth issues?**
- Use Personal Access Token instead of password
- Go to GitHub Settings → Developer settings → Personal access tokens
- Generate new token, use it instead of password

**Render deployment failing?**
- Check logs in Render dashboard
- Verify `Procfile` exists
- Verify `gunicorn` is in requirements.txt

---

## 📋 Checklist

- [ ] Git installed and verified
- [ ] GitHub account created
- [ ] GitHub repo created and named `classroom-timetable`
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Repo connected to Render
- [ ] App deployed to Render
- [ ] Visiting your live URL works
- [ ] All features working online

---

**Once deployment is done, your app is live for everyone to use!** 🌐✨
