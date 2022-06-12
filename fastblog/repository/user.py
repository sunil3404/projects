import pathlib
import sys
sys.path.append(pathlib.Path(__file__).parent.resolve())
import models, database, db_model
from hashing import Hash
from fastapi import HTTPException, status

def create(request, db):
    new_user = db_model.Users(name=request.name,
                              email=request.email,
                              password=Hash.encrypt(request.password)
                              )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db):
    user = db.query(db_model.Users).filter(db_model.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exist")
    return user