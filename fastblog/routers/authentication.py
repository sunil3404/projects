from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException, status
import pathlib
import sys
from requests import Session
sys.path.append(pathlib.Path(__file__).parent.resolve())
import models, db_model, database
from hashing import Hash


router = APIRouter(
    tags=["Login"]

)


@router.post("/login")
def login(request : models.Login, db : Session =  Depends(database.get_db)):
    user = db.query(db_model.Users).filter(db_model.Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    return user