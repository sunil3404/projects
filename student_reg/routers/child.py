from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Child
import database
import schemas

router = APIRouter()


@router.post("/create_child")
def create_child(request : schemas.Child_Show, db : Session = Depends(database.get_db)):

    #parent_id = db.query(Parent).filter(Parent.p_id == request.p_id).first()
    new_child = Child(parent_id = request.parent_id)

    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    return new_child

@router.get("/fetch_child")
def fetch_child(db : Session = Depends(database.get_db)):
    child = db.query(Child).all()

    return child

@router.delete("/delete/{child_id}")
def delete_child(child_id, db : Session = Depends(database.get_db)):

    child = db.query(Child).filter(Child.child_id == child_id).first()
    if not child:
        raise HTTPException(status_code = 404, detail="Not found")

    db.query(Child).filter(Child.child_id == child_id).\
       delete(synchronize_session = False)

    db.commit()
    return "Deleted succsess"
