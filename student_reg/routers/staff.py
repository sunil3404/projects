from fastapi import Depends, HTTPException, APIRouter
from models import Staff, Department, Student
from schemas import Staff_Reg
from sqlalchemy.orm import Session
from repository import staff
import database



router = APIRouter()

@router.post("/create_staff")
def create_new_staff_appointment(request : Staff_Reg, 
                                 db:Session = Depends(database.get_db)):
    dept = db.query(Department).filter(Department.dept_name == request.staff_dept).first()
    if dept:
        new_staff = staff.create_staff(db, dept, request)
    else:
        raise HTTPException(status_code=404, 
                            detail=f"department {request.staff_dept} does not exist")
    return new_staff


