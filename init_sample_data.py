"""
Sample data initialization script for Classroom & Timetable Monitoring System
Run this after starting the app to populate with sample data for testing.

Usage:
    python init_sample_data.py
"""

from app import app, db
from models import Classroom, Teacher, Student, TimeTable, Enrollment

def init_sample_data():
    """Initialize database with sample data"""
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        print("✓ Database cleared and recreated")
        
        # Add Classrooms
        classrooms = [
            Classroom(name='A101', capacity=30, location='Building A, Floor 1'),
            Classroom(name='A102', capacity=35, location='Building A, Floor 1'),
            Classroom(name='B201', capacity=25, location='Building B, Floor 2'),
            Classroom(name='Lab-01', capacity=20, location='Science Building'),
        ]
        db.session.add_all(classrooms)
        print("✓ Added 4 classrooms")
        
        # Add Teachers
        teachers = [
            Teacher(name='Dr. John Smith', email='john.smith@school.com', 
                   phone='+1234567890', department='Mathematics'),
            Teacher(name='Ms. Sarah Johnson', email='sarah.johnson@school.com', 
                   phone='+1234567891', department='Science'),
            Teacher(name='Mr. David Lee', email='david.lee@school.com', 
                   phone='+1234567892', department='English'),
            Teacher(name='Dr. Emily Chen', email='emily.chen@school.com', 
                   phone='+1234567893', department='Physics'),
        ]
        db.session.add_all(teachers)
        print("✓ Added 4 teachers")
        
        # Add Students
        students = [
            Student(name='Alice Brown', email='alice.brown@student.com', 
                   roll_number='2024001', phone='+1111111111'),
            Student(name='Bob Wilson', email='bob.wilson@student.com', 
                   roll_number='2024002', phone='+1111111112'),
            Student(name='Charlie Davis', email='charlie.davis@student.com', 
                   roll_number='2024003', phone='+1111111113'),
            Student(name='Diana Anderson', email='diana.anderson@student.com', 
                   roll_number='2024004', phone='+1111111114'),
            Student(name='Eve Taylor', email='eve.taylor@student.com', 
                   roll_number='2024005', phone='+1111111115'),
            Student(name='Frank Miller', email='frank.miller@student.com', 
                   roll_number='2024006', phone='+1111111116'),
        ]
        db.session.add_all(students)
        print("✓ Added 6 students")
        
        db.session.commit()
        
        # Add Timetables
        timetables = [
            TimeTable(classroom_id=1, teacher_id=1, subject='Calculus-I',
                     day_of_week='Monday', start_time='09:00', end_time='10:30'),
            TimeTable(classroom_id=1, teacher_id=1, subject='Calculus-I',
                     day_of_week='Wednesday', start_time='09:00', end_time='10:30'),
            TimeTable(classroom_id=2, teacher_id=2, subject='Physics-Basics',
                     day_of_week='Monday', start_time='11:00', end_time='12:30'),
            TimeTable(classroom_id=2, teacher_id=2, subject='Physics-Basics',
                     day_of_week='Thursday', start_time='11:00', end_time='12:30'),
            TimeTable(classroom_id=3, teacher_id=3, subject='English-Literature',
                     day_of_week='Tuesday', start_time='14:00', end_time='15:30'),
            TimeTable(classroom_id=4, teacher_id=4, subject='Quantum Physics Lab',
                     day_of_week='Friday', start_time='10:00', end_time='12:00'),
        ]
        db.session.add_all(timetables)
        db.session.commit()
        print("✓ Added 6 timetable entries")
        
        # Add Enrollments
        enrollments = [
            # Calculus-I enrollments
            Enrollment(student_id=1, timetable_id=1),
            Enrollment(student_id=2, timetable_id=1),
            Enrollment(student_id=3, timetable_id=1),
            Enrollment(student_id=1, timetable_id=2),
            Enrollment(student_id=2, timetable_id=2),
            
            # Physics-Basics enrollments
            Enrollment(student_id=4, timetable_id=3),
            Enrollment(student_id=5, timetable_id=3),
            Enrollment(student_id=6, timetable_id=3),
            
            # English-Literature enrollments
            Enrollment(student_id=1, timetable_id=5),
            Enrollment(student_id=4, timetable_id=5),
            
            # Lab enrollments
            Enrollment(student_id=2, timetable_id=6),
            Enrollment(student_id=5, timetable_id=6),
        ]
        db.session.add_all(enrollments)
        db.session.commit()
        print("✓ Added 12 student enrollments")
        
        print("\n" + "="*50)
        print("✓ Sample data initialization completed!")
        print("="*50)
        print("\nYou can now login with the following test credentials:")
        print("\nClassrooms:")
        for c in classrooms:
            print(f"  - {c.name} (Capacity: {c.capacity})")
        
        print("\nTeachers:")
        for t in teachers:
            print(f"  - {t.name} ({t.department})")
        
        print("\nStudents:")
        for s in students:
            print(f"  - {s.name} (Roll: {s.roll_number})")
        
        print("\n" + "="*50)
        print("Now access the application at: http://localhost:5000")
        print("="*50 + "\n")

if __name__ == '__main__':
    init_sample_data()
