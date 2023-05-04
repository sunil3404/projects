from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Parent, Child
import database
import schemas

router = APIRouter()


@router.post("/create_parent")
def create_parent(request : schemas.Parent_Show, db : Session = Depends(database.get_db)):

    new_parent = Parent(pname = request.pname)

    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)

    return new_parent

@router.get("/fetch_parebt")
def fetch_parent(db : Session = Depends(database.get_db)):
    parent = db.query(Parent).all()
    return parent

@router.delete("/delete/{parent_id}")
def delete_parent(parent_id : int, db : Session = Depends(database.get_db)):

    p = db.query(Parent).filter(Parent.id == parent_id).first()
    if not p:
        raise HTTPException(status_code = 404, detail="Not FOunf")

    db.query(Parent).filter(Parent.id == parent_id).\
       delete(synchronize_session=False)
    db.commit()
    db.flush()
    return f"parent with id {parent_id} deleted"
