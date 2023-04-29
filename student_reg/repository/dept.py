from models import Department

def create_department(db, request):
    try:
        new_dp = Department(dept_name=request.dept_name, 
                            dept_abr=request.dept_abr)
        db.add(new_dp)
        db.commit()
        db.refresh(new_dp)
    except Exception as ex:
        print(new_dp)
    return new_dp

def fetch_all_department(db):
    dept = db.query(Department).all()
    return  dept

def update_department_abreviation(db, request, dept_id):
    db.query(Department).filter(Department.dept_id == dept_id).\
            update({Department.dept_abr : request.dept_abr,
                Department.dept_name : request.dept_name}, synchronize_session=False)
    db.commit()
    return "updated"
