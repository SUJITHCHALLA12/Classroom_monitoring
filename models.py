from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Classroom(db.Model):
    """Model for Classroom"""
    __tablename__ = 'classroom'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    timetables = db.relationship('TimeTable', backref='classroom', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Classroom {self.name}>'


class Teacher(db.Model):
    """Model for Teacher"""
    __tablename__ = 'teacher'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    timetables = db.relationship('TimeTable', backref='teacher', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Teacher {self.name}>'


class Student(db.Model):
    """Model for Student"""
    __tablename__ = 'student'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    enrollments = db.relationship('Enrollment', backref='student', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Student {self.name}>'


class TimeTable(db.Model):
    """Model for TimeTable entry"""
    __tablename__ = 'timetable'
    
    id = db.Column(db.Integer, primary_key=True)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)  # Monday, Tuesday, etc.
    start_time = db.Column(db.String(10), nullable=False)  # HH:MM format
    end_time = db.Column(db.String(10), nullable=False)    # HH:MM format
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    enrollments = db.relationship('Enrollment', backref='timetable', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<TimeTable {self.subject} {self.day_of_week}>'
    
    def is_ongoing(self):
        """Check if class is currently ongoing"""
        from datetime import datetime
        from datetime import datetime as dt
        
        current_time = dt.now().strftime('%H:%M')
        current_day = dt.now().strftime('%A')
        
        return (current_day == self.day_of_week and 
                self.start_time <= current_time <= self.end_time and 
                self.is_active)


class Enrollment(db.Model):
    """Model for Student Enrollment in TimeTable"""
    __tablename__ = 'enrollment'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    timetable_id = db.Column(db.Integer, db.ForeignKey('timetable.id'), nullable=False)
    is_present = db.Column(db.Boolean, default=None)  # None = unmarked, True = present, False = absent
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_marked_at = db.Column(db.DateTime)
    
    __table_args__ = (db.UniqueConstraint('student_id', 'timetable_id', name='unique_student_timetable'),)
    
    def __repr__(self):
        return f'<Enrollment Student {self.student_id} - TimeTable {self.timetable_id}>'
