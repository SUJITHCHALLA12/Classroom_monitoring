# 🚀 Quick Start Guide

Get your Classroom & Timetable Monitoring System up and running in just 3 minutes!

## Step 1: Install Dependencies (1 minute)

Open **PowerShell** or **Command Prompt** and run:

```powershell
cd C:\Users\rohith\ClassroomTimetable
pip install -r requirements.txt
```

Expected output:
```
Successfully installed Flask Flask-SQLAlchemy SQLAlchemy Werkzeug
```

## Step 2: Load Sample Data (Optional but Recommended!)

Run this command to populate the database with sample data for testing:

```powershell
python init_sample_data.py
```

Expected output:
```
✓ Database cleared and recreated
✓ Added 4 classrooms
✓ Added 4 teachers
✓ Added 6 students
✓ Added 6 timetable entries
✓ Added 12 student enrollments

✓ Sample data initialization completed!
```

## Step 3: Start the Application (1 minute)

```powershell
python app.py
```

Expected output:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

## Step 4: Open in Browser

Click this link or copy-paste into your browser:
```
http://localhost:5000
```

## 🎉 You're Done!

The application is now running with sample data. Try these actions:

### Dashboard (Home)
- View overview statistics
- See ongoing classes in real-time

### Classrooms
- View all classrooms
- Add new classrooms
- Check class schedules
- Click on any classroom for details

### Teachers
- View all teachers
- Add new teachers
- Check their schedules
- View classes assigned

### Students
- View all students
- Add new students
- Check enrollment status
- View attendance

### Timetables
- View all class schedules
- Create new timetables with automatic conflict detection
- Manage student enrollments
- Mark attendance for students

## Sample Test Data

### Classrooms
- A101 (30 students) - Building A, Floor 1
- A102 (35 students) - Building A, Floor 1
- B201 (25 students) - Building B, Floor 2
- Lab-01 (20 students) - Science Building

### Teachers
- Dr. John Smith (Mathematics)
- Ms. Sarah Johnson (Science)
- Mr. David Lee (English)
- Dr. Emily Chen (Physics)

### Students
- Alice Brown, Bob Wilson, Charlie Davis
- Diana Anderson, Eve Taylor, Frank Miller

### Sample Classes
- **Calculus-I** - Mon & Wed 9:00-10:30 AM - Classroom A101
- **Physics-Basics** - Mon & Thu 11:00 AM-12:30 PM - Classroom A102
- **English-Literature** - Tue 2:00-3:30 PM - Classroom B201
- **Quantum Physics Lab** - Fri 10:00 AM-12:00 PM - Lab-01

## Common Tasks

### Mark Attendance
1. Click **Timetables** → Select a class → Click **View**
2. Find the student and click the status button
3. Attendance is marked immediately

### Enroll Student in Class
1. Go to **Timetables** → Click **View** on a class
2. Click **Add Student** button
3. Select student from dropdown → Click **Add to Class**

### Create New Class Schedule
1. Click **Timetables** → Click **Add Timetable**
2. Select classroom, teacher, subject, day, and time
3. System checks for conflicts automatically
4. Click **Add Timetable**

### Check Classroom Availability
1. Click **Classrooms** → View any classroom
2. See all upcoming classes for that classroom
3. Use API: `http://localhost:5000/api/classroom-availability/1`

## Keyboard Shortcuts

- `Ctrl+K` - Focus on search (if implemented)
- `Ctrl+S` - Save form (in supported browsers)

## Troubleshooting

**Q: Port 5000 already in use**
A: Edit the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

**Q: Module not found error**
A: Make sure you ran `pip install -r requirements.txt`

**Q: Database errors**
A: Delete `classroom_timetable.db` file and restart the app

**Q: Can't access localhost:5000**
A: Make sure the Flask server is running and no firewall is blocking it

## Next Steps

1. ✅ Explore the application with sample data
2. Create your own classrooms, teachers, and students
3. Set up timetables
4. Track attendance
5. Read [README.md](README.md) for advanced features
6. Customize CSS in `static/css/style.css`
7. Add more features as needed

## Stop the Application

Press `Ctrl+C` in the terminal to stop the server.

---

**Need help?** Check the complete [README.md](README.md) documentation.

**Happy scheduling! 📚**
