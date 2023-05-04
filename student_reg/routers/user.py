from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
import database
from models import User, Posts
import schemas
from typing import List
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

router = APIRouter()

@router.post("/create_user")
def create_user(request :  schemas.User, db : Session = Depends(database.get_db)):
    
    hashed_password = get_password_hash(request.password)
    email = db.query(User).filter(User.email == request.email).first()
    if email :
        raise HTTPException(status_code=302, detail= f"{request.email} already exists")
    new_user = User(username = request.username, password = hashed_password, 
                    email = request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/fetch_user", response_model=List[schemas.ShowUser])
def fetch_user(db : Session = Depends(database.get_db)):
    all_user = db.query(User).all()
    return all_user

@router.put("/update/{user_id}")
def update_email(user_id, request : schemas.User, db : Session = Depends(database.get_db)):
    
    print(request.email, user_id)
    db.query(User).filter(User.user_id == user_id).\
       update({User.email : request.email}, synchronize_session=False)

    db.commit()
    return "Succesfully Updated Email"

@router.delete("/delete/{user_id}")
def delete_user(user_id, db : Session = Depends(database.get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"{user_id} does not exist")

    db.query(User).filter(User.user_id == user_id).\
      delete(synchronize_session=False)
    db.commit()
    return f"User {user_id}deleted successfully"
