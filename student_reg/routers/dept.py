from fastapi import APIRouter, Depends, HTTPException
import schemas, models
import database
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from repository import dept as deptrep 
from typing import List


router = APIRouter()

@router.post("/create_dept", response_model=schemas.Show_Department)
def create_dept(request : schemas.Department_Reg, db : Session = Depends(database.get_db)):
    new_dp = deptrep.create_department(db, request)
    return new_dp

@router.get("/fetch_dept", response_model=List[schemas.Show_Department])
def fetch_all_department(db : Session = Depends(database.get_db)):
    all_dept = deptrep.fetch_all_department(db)
    return  all_dept

@router.get("/dept/{dept_id}", response_model=schemas.Show_Department)
def fetch_department_by_id(dept_id, db : Session = Depends(database.get_db)):
    dept = db.query(models.Department).filter(models.Department.dept_id == dept_id).first()

    return dept

@router.put("/{dept_id}")
def update_department_abreviation(dept_id, request : schemas.Department_Reg, 
                                  db : Session = Depends(database.get_db)):
    dept = db.query(models.Department).filter(models.Department.dept_id == dept_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail=f"dept with id {dept_id} does not exist")
    else:
        update_message = deptrep.update_department_abreviation(db, request, dept_id)
    return "updated"
