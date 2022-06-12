from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException, status
import pathlib, sys, jwt_token, models, db_model, database
from requests import Session
sys.path.append(pathlib.Path(__file__).parent.resolve())
from hashing import Hash
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session =  Depends(database.get_db)):
    user = db.query(db_model.Users).filter(db_model.Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    access_token = jwt_token.create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}