from fastapi import APIRouter, Depends, HTTPException
from schemas import Blogs, User, ShowUser
import models, schemas
import hashing
import database
from typing import List
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
import oauthtoken as oauth

database.Base.metadata.create_all(bind=engine)

router = APIRouter(
	prefix='/user',
	tags=['Users']
)

@router.get("/", response_model = List[schemas.ShowUser])
async def all_users(db: SessionLocal = Depends(database.get_db)):
	user = db.query(models.User).all()
	if not user:
		raise HTTPException(status_code=404, detail="No Users Found")
	return user

@router.get("/{id}", response_model=schemas.ShowUser)
async def user_by_id(id : int, db: SessionLocal = Depends(database.get_db)):
	user = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code=404, detail=f"No User with id -> {id} exists.")
	return user

@router.post("/create", response_model=schemas.ShowUser)
async def create(request: User, db : SessionLocal = Depends(database.get_db), current_user :  OAuth2PasswordRequestForm = Depends(oauth.get_current_user)):
	user = models.User(email=request.email, hashed_password = hashing.get_password_hash(request.hashed_password))
	db.add(user)
	db.commit()
	db.refresh(user)
	return user