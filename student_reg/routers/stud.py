from fastapi import APIRouter, Depends, HTTPException
import schemas, models
from database import SessionLocal
import database
from sqlalchemy.orm import Session
from models import Department, Student
from repository import stud as stud_rep
from typing import Any, List


router = APIRouter()

@router.post("/create_students")
def create_student(student : schemas.Students_Registration, 
                   db: Session = Depends(database.get_db)):
    #dept = db.query(Department).filter(Department.dept_name == student.dept_name).first()
    dept = db.query(Department).filter(Department.dept_id == student.dept_id).first()
    if dept:
        new_stud = stud_rep.create_student(db, student, dept)
    else:
        raise HTTPException(status_code=404, detail=f"{student.dept_name} department does not exist")
    return new_stud

@router.get("/all_student", response_model=List[schemas.Show_Student])
def fetch_all_students(db: Session = Depends(database.get_db)):
    all_students = stud_rep.fetch_all_students(db)
    return all_students 

@router.get("/{id}", response_model=schemas.Show_Student)
def fetch_student_by_id(id, db : Session = Depends(database.get_db)) -> Any:
    student = stud_rep.fetch_student_by_id(db, id)
    
    if not student:
        raise HTTPException(status_code=404, detail=f"student with id {id} does not exist")
    return student


@router.get("/gender/{gender}", response_model = schemas.Show_Student)
def fetch_students_by_gender(gender, db : Session = Depends(database.get_db)):
    students = stud_rep.fetch_students_by_gender(db, gender)
    if not students:
        raise HTTPException(status_code=404, detail=f"No student exists with gender as {gender}")
    return students



