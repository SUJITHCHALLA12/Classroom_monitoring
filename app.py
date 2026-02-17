from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Classroom, Teacher, Student, TimeTable, Enrollment
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classroom_timetable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Initialize Database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


# Routes

@app.route('/')
def index():
    """Dashboard - Overview of the system"""
    total_classrooms = Classroom.query.count()
    total_teachers = Teacher.query.count()
    total_students = Student.query.count()
    active_sessions = TimeTable.query.filter_by(is_active=True).count()
    
    # Get ongoing classes
    ongoing_classes = []
    current_time = datetime.now().strftime('%H:%M')
    current_day = datetime.now().strftime('%A')
    
    timetables = TimeTable.query.filter_by(is_active=True).all()
    for tt in timetables:
        if tt.start_time <= current_time <= tt.end_time and tt.day_of_week == current_day:
            ongoing_classes.append({
                'subject': tt.subject,
                'classroom': tt.classroom.name,
                'teacher': tt.teacher.name,
                'start_time': tt.start_time,
                'end_time': tt.end_time
            })
    
    return render_template('index.html', 
                         total_classrooms=total_classrooms,
                         total_teachers=total_teachers,
                         total_students=total_students,
                         active_sessions=active_sessions,
                         ongoing_classes=ongoing_classes)


# CLASSROOM ROUTES
@app.route('/classrooms')
def classrooms():
    """View all classrooms"""
    classrooms = Classroom.query.all()
    return render_template('classrooms.html', classrooms=classrooms)


@app.route('/classroom/add', methods=['GET', 'POST'])
def add_classroom():
    """Add new classroom"""
    if request.method == 'POST':
        name = request.form.get('name')
        capacity = request.form.get('capacity')
        location = request.form.get('location')
        
        if not name or not capacity:
            flash('Name and capacity are required!', 'error')
            return redirect(url_for('add_classroom'))
        
        classroom = Classroom(name=name, capacity=int(capacity), location=location)
        db.session.add(classroom)
        db.session.commit()
        
        flash(f'Classroom {name} added successfully!', 'success')
        return redirect(url_for('classrooms'))
    
    return render_template('add_classroom.html')


@app.route('/classroom/<int:id>')
def classroom_detail(id):
    """View classroom details"""
    classroom = Classroom.query.get_or_404(id)
    timetables = classroom.timetables
    return render_template('classroom_detail.html', classroom=classroom, timetables=timetables)


@app.route('/classroom/<int:id>/delete', methods=['POST'])
def delete_classroom(id):
    """Delete classroom"""
    classroom = Classroom.query.get_or_404(id)
    name = classroom.name
    db.session.delete(classroom)
    db.session.commit()
    
    flash(f'Classroom {name} deleted!', 'success')
    return redirect(url_for('classrooms'))


# TEACHER ROUTES
@app.route('/teachers')
def teachers():
    """View all teachers"""
    teachers = Teacher.query.all()
    return render_template('teachers.html', teachers=teachers)


@app.route('/teacher/add', methods=['GET', 'POST'])
def add_teacher():
    """Add new teacher"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        department = request.form.get('department')
        
        if not name or not email:
            flash('Name and email are required!', 'error')
            return redirect(url_for('add_teacher'))
        
        existing = Teacher.query.filter_by(email=email).first()
        if existing:
            flash('Teacher with this email already exists!', 'error')
            return redirect(url_for('add_teacher'))
        
        teacher = Teacher(name=name, email=email, phone=phone, department=department)
        db.session.add(teacher)
        db.session.commit()
        
        flash(f'Teacher {name} added successfully!', 'success')
        return redirect(url_for('teachers'))
    
    return render_template('add_teacher.html')


@app.route('/teacher/<int:id>')
def teacher_detail(id):
    """View teacher details"""
    teacher = Teacher.query.get_or_404(id)
    timetables = teacher.timetables
    return render_template('teacher_detail.html', teacher=teacher, timetables=timetables)


@app.route('/teacher/<int:id>/delete', methods=['POST'])
def delete_teacher(id):
    """Delete teacher"""
    teacher = Teacher.query.get_or_404(id)
    name = teacher.name
    db.session.delete(teacher)
    db.session.commit()
    
    flash(f'Teacher {name} deleted!', 'success')
    return redirect(url_for('teachers'))


# STUDENT ROUTES
@app.route('/students')
def students():
    """View all students"""
    students = Student.query.all()
    return render_template('students.html', students=students)


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    """Add new student"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        roll_number = request.form.get('roll_number')
        phone = request.form.get('phone')
        
        if not name or not email or not roll_number:
            flash('Name, email, and roll number are required!', 'error')
            return redirect(url_for('add_student'))
        
        existing_email = Student.query.filter_by(email=email).first()
        existing_roll = Student.query.filter_by(roll_number=roll_number).first()
        
        if existing_email:
            flash('Student with this email already exists!', 'error')
            return redirect(url_for('add_student'))
        
        if existing_roll:
            flash('Student with this roll number already exists!', 'error')
            return redirect(url_for('add_student'))
        
        student = Student(name=name, email=email, roll_number=roll_number, phone=phone)
        db.session.add(student)
        db.session.commit()
        
        flash(f'Student {name} added successfully!', 'success')
        return redirect(url_for('students'))
    
    return render_template('add_student.html')


@app.route('/student/<int:id>')
def student_detail(id):
    """View student details"""
    student = Student.query.get_or_404(id)
    enrollments = student.enrollments
    return render_template('student_detail.html', student=student, enrollments=enrollments)


@app.route('/student/<int:id>/delete', methods=['POST'])
def delete_student(id):
    """Delete student"""
    student = Student.query.get_or_404(id)
    name = student.name
    db.session.delete(student)
    db.session.commit()
    
    flash(f'Student {name} deleted!', 'success')
    return redirect(url_for('students'))


# TIMETABLE ROUTES
@app.route('/timetables')
def timetables():
    """View all timetables"""
    timetables = TimeTable.query.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('timetables.html', timetables=timetables, days=days)


@app.route('/timetable/add', methods=['GET', 'POST'])
def add_timetable():
    """Add new timetable entry"""
    classrooms = Classroom.query.all()
    teachers = Teacher.query.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if request.method == 'POST':
        classroom_id = request.form.get('classroom_id')
        teacher_id = request.form.get('teacher_id')
        subject = request.form.get('subject')
        day_of_week = request.form.get('day_of_week')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        
        if not all([classroom_id, teacher_id, subject, day_of_week, start_time, end_time]):
            flash('All fields are required!', 'error')
            return redirect(url_for('add_timetable'))
        
        # Check for conflicts
        existing = TimeTable.query.filter_by(
            classroom_id=int(classroom_id),
            day_of_week=day_of_week,
            is_active=True
        ).all()
        
        for tt in existing:
            if not (end_time <= tt.start_time or start_time >= tt.end_time):
                flash('Classroom is already booked for this time!', 'error')
                return redirect(url_for('add_timetable'))
        
        timetable = TimeTable(
            classroom_id=int(classroom_id),
            teacher_id=int(teacher_id),
            subject=subject,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(timetable)
        db.session.commit()
        
        flash(f'Timetable entry for {subject} added successfully!', 'success')
        return redirect(url_for('timetables'))
    
    return render_template('add_timetable.html', classrooms=classrooms, teachers=teachers, days=days)


@app.route('/timetable/<int:id>/delete', methods=['POST'])
def delete_timetable(id):
    """Delete timetable entry"""
    timetable = TimeTable.query.get_or_404(id)
    subject = timetable.subject
    db.session.delete(timetable)
    db.session.commit()
    
    flash(f'Timetable entry for {subject} deleted!', 'success')
    return redirect(url_for('timetables'))


# ENROLLMENT ROUTES
@app.route('/enrollment/add/<int:timetable_id>', methods=['GET', 'POST'])
def add_enrollment(timetable_id):
    """Add student enrollment to timetable"""
    timetable = TimeTable.query.get_or_404(timetable_id)
    students = Student.query.all()
    
    # Get already enrolled students
    enrolled_ids = [e.student_id for e in timetable.enrollments]
    available_students = [s for s in students if s.id not in enrolled_ids]
    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        
        if not student_id:
            flash('Student is required!', 'error')
            return redirect(url_for('add_enrollment', timetable_id=timetable_id))
        
        enrollment = Enrollment(student_id=int(student_id), timetable_id=timetable_id)
        db.session.add(enrollment)
        db.session.commit()
        
        flash('Student enrolled successfully!', 'success')
        return redirect(url_for('timetable_detail', id=timetable_id))
    
    return render_template('add_enrollment.html', timetable=timetable, available_students=available_students)


@app.route('/timetable/<int:id>')
def timetable_detail(id):
    """View timetable details with enrolled students"""
    timetable = TimeTable.query.get_or_404(id)
    enrollments = timetable.enrollments
    return render_template('timetable_detail.html', timetable=timetable, enrollments=enrollments)


@app.route('/enrollment/<int:enrollment_id>/mark', methods=['POST'])
def mark_attendance(enrollment_id):
    """Mark attendance"""
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    is_present = request.form.get('is_present') == 'true'
    
    enrollment.is_present = is_present
    enrollment.last_marked_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Attendance marked!'})


@app.route('/enrollment/<int:id>/delete', methods=['POST'])
def delete_enrollment(id):
    """Remove student enrollment"""
    enrollment = Enrollment.query.get_or_404(id)
    timetable_id = enrollment.timetable_id
    student_name = enrollment.student.name
    
    db.session.delete(enrollment)
    db.session.commit()
    
    flash(f'Student {student_name} removed from enrollment!', 'success')
    return redirect(url_for('timetable_detail', id=timetable_id))


# API ENDPOINTS

@app.route('/api/classroom-availability/<int:classroom_id>')
def classroom_availability(classroom_id):
    """Get real-time classroom availability"""
    classroom = Classroom.query.get_or_404(classroom_id)
    current_time = datetime.now().strftime('%H:%M')
    current_day = datetime.now().strftime('%A')
    
    # Check if any class is ongoing
    ongoing = TimeTable.query.filter_by(
        classroom_id=classroom_id,
        day_of_week=current_day,
        is_active=True
    ).filter(
        TimeTable.start_time <= current_time,
        TimeTable.end_time >= current_time
    ).first()
    
    status = {
        'classroom_id': classroom_id,
        'classroom_name': classroom.name,
        'is_available': ongoing is None,
        'current_time': current_time,
        'current_day': current_day,
        'ongoing_class': {
            'subject': ongoing.subject,
            'teacher': ongoing.teacher.rohith,
            'start_time': ongoing.start_time,
            'end_time': ongoing.end_time
        } if ongoing else None
    }
    
    return jsonify(status)


@app.route('/api/schedule/<int:teacher_id>')
def teacher_schedule(teacher_id):
    """Get teacher's schedule for the week"""
    teacher = Teacher.query.get_or_404(teacher_id)
    schedule = []
    
    for tt in teacher.timetables:
        if tt.is_active:
            schedule.append({
                'subject': tt.subject,
                'classroom': tt.classroom.name,
                'day': tt.day_of_week,
                'start_time': tt.start_time,
                'end_time': tt.end_time
            })
    
    return jsonify({'teacher': teacher.name, 'schedule': schedule})


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
