from models import Staff

def create_staff(db, dept, request):
    new_staff = Staff(staff_name = request.staff_name,
                      dept_id = dept.dept_id,
                      staff_designation = request.staff_designation,
                      department = dept)
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

