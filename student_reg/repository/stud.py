import models

def create_student(db, student, dept):
    new_stud = models.Student(name=student.name, mdept = dept,
                               age=student.age, sex=student.sex)
    db.add(new_stud)
    db.commit()
    db.refresh(new_stud)
    return new_stud

def fetch_all_students(db):
    all_students = db.query(models.Student).all()
    return all_students 

def fetch_student_by_id(db,id):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    print(type(student))
    return student

def fetch_students_by_dept_name(db, depat_id):
    student = db.query(models.Student).filter(models.Student.dept_id == depat_id).all()
    return student

def fetch_students_by_gender(db, gender):
    students = db.query(models.Student).filter(models.Student.sex == gender.capitalize()).all()
    return students



