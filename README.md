# Classroom & Timetable Monitoring Web Application

A comprehensive web application for managing classrooms, timetables, teachers, and students with real-time monitoring and attendance tracking capabilities.

## Features

### Core Features
- ✅ **Classroom Management** - Add, view, and manage classrooms with capacity information
- ✅ **Teacher Management** - Manage teacher profiles, departments, and contact information
- ✅ **Student Management** - Register students with roll numbers and contact details
- ✅ **Timetable Management** - Create and manage class schedules with conflict detection
- ✅ **Student Enrollment** - Enroll students in classes
- ✅ **Attendance Tracking** - Mark and monitor student attendance
- ✅ **Real-time Classroom Availability** - Check which classrooms are currently in use
- ✅ **Dashboard Overview** - Quick statistics and ongoing classes display
- ✅ **Conflict Detection** - Prevents double-booking of classrooms

## Technology Stack

- **Backend**: Flask 3.0.0 (Python Web Framework)
- **Database**: SQLite (Lightweight, file-based database)
- **Frontend**: HTML5, CSS3, JavaScript
- **ORM**: SQLAlchemy for database operations
- **Icons**: Font Awesome 6.0

## Project Structure

```
ClassroomTimetable/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── requirements.txt      # Project dependencies
├── classroom_timetable.db # SQLite database (auto-generated)
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Dashboard
│   ├── classrooms.html  # Classroom listing
│   ├── add_classroom.html
│   ├── classroom_detail.html
│   ├── teachers.html
│   ├── add_teacher.html
│   ├── teacher_detail.html
│   ├── students.html
│   ├── add_student.html
│   ├── student_detail.html
│   ├── timetables.html
│   ├── add_timetable.html
│   ├── timetable_detail.html
│   ├── add_enrollment.html
│   ├── 404.html         # Error page
│   └── 500.html         # Server error page
└── static/
    ├── css/
    │   └── style.css    # Main stylesheet
    └── js/
        └── script.js    # JavaScript functionality
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

Open PowerShell or Command Prompt and navigate to the project directory:

```powershell
cd C:\Users\rohith\ClassroomTimetable
pip install -r requirements.txt
```

### Step 2: Run the Application

```powershell
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 3: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

## Usage Guide

### Dashboard
The home page displays:
- Total number of classrooms, teachers, students, and active sessions
- Real-time list of ongoing classes
- Quick action buttons to add new entities

### Managing Classrooms
1. Click **Classrooms** in the navigation bar
2. Click **Add Classroom** to add a new classroom
3. Fill in classroom name, capacity, and location
4. Click **Add Classroom** to save

### Managing Teachers
1. Click **Teachers** in the navigation bar
2. Click **Add Teacher** to register a new teacher
3. Fill in name, email, department, and phone
4. Click **Add Teacher** to save

### Managing Students
1. Click **Students** in the navigation bar
2. Click **Add Student** to register a new student
3. Fill in name, roll number, email, and phone
4. Click **Add Student** to save

### Creating Timetables
1. Click **Timetables** in the navigation bar
2. Click **Add Timetable** to create a class schedule
3. Select classroom, teacher, subject, day, and time
4. The system will detect conflicts automatically
5. Click **Add Timetable** to save

### Enrolling Students
1. View a timetable entry by clicking on a class
2. Click **Add Student** button
3. Select a student from the dropdown
4. Click **Add to Class** to enroll

### Marking Attendance
1. View a timetable entry
2. Click the **Mark** button next to each student
3. The attendance status will update immediately

## Database Models

### Classroom
- `id`: Primary key
- `name`: Unique classroom name
- `capacity`: Student capacity
- `location`: Physical location
- `created_at`: Timestamp

### Teacher
- `id`: Primary key
- `name`: Teacher name
- `email`: Unique email address
- `phone`: Contact number
- `department`: Department name
- `created_at`: Timestamp

### Student
- `id`: Primary key
- `name`: Student name
- `email`: Unique email address
- `roll_number`: Unique roll number
- `phone`: Contact number
- `created_at`: Timestamp

### TimeTable
- `id`: Primary key
- `classroom_id`: Foreign key to Classroom
- `teacher_id`: Foreign key to Teacher
- `subject`: Subject name
- `day_of_week`: Day (Monday-Sunday)
- `start_time`: Class start time (HH:MM)
- `end_time`: Class end time (HH:MM)
- `is_active`: Schedule status
- `created_at`: Timestamp

### Enrollment
- `id`: Primary key
- `student_id`: Foreign key to Student
- `timetable_id`: Foreign key to TimeTable
- `is_present`: Attendance status (True/False/None)
- `enrollment_date`: Enrollment timestamp
- `last_marked_at`: Last attendance update

## API Endpoints

### Classroom Availability
```
GET /api/classroom-availability/<classroom_id>
```
Returns real-time availability status of a classroom.

### Teacher Schedule
```
GET /api/schedule/<teacher_id>
```
Returns the weekly schedule for a teacher.

## Features Highlights

### Conflict Detection
The system automatically checks for double-bookings when creating timetables. If a classroom is already booked during the requested time, you'll receive an error message.

### Real-time Monitoring
- Dashboard shows ongoing classes in real-time
- Classroom availability API provides live status
- Attendance can be marked immediately

### User-Friendly Interface
- Clean, modern design with intuitive navigation
- Responsive layout that works on desktop and mobile devices
- Confirmation dialogs for delete operations
- Success/error alert messages
- Icons for better visual clarity

## Customization

### Change Secret Key
Edit `app.py` and replace:
```python
app.config['SECRET_KEY'] = 'change-this-to-a-secure-random-string'
```

### Modify Styling
Edit `static/css/style.css` to customize colors, fonts, and layout.

### Add New Features
1. Create new database models in `models.py`
2. Add routes in `app.py`
3. Create corresponding HTML templates in `templates/`

## Troubleshooting

### Database Already Exists Error
Delete `classroom_timetable.db` and run the app again to start fresh.

### Port Already in Use
If port 5000 is already in use, modify the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or any available port
```

### Import Errors
Make sure all dependencies are installed:
```powershell
pip install -r requirements.txt
```

## Security Considerations

⚠️ **This application is for development/educational purposes only.**

For production:
1. Change `SECRET_KEY` to a secure random string
2. Set `debug=False`
3. Use a production-grade database (PostgreSQL, MySQL)
4. Implement user authentication
5. Add input validation and sanitization
6. Use HTTPS
7. Implement role-based access control

## Future Enhancements

- User authentication and authorization
- Email notifications for schedule changes
- Advanced reporting and analytics
- Student performance tracking
- Parent portal
- Mobile app
- SMS notifications
- Integration with external calendar systems

## Support & Documentation

For more information about Flask, visit: https://flask.palletsprojects.com/
For SQLAlchemy documentation: https://docs.sqlalchemy.org/

## License

This project is open source and available for educational use.

## Author

Created: February 2026

---

**Happy scheduling! 📚**
