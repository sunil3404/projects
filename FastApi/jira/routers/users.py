from fastapi import APIRouter, Depends, HTTPException
import schemas, models
import database
from database import SessionLocal
import hashing
from typing import List



router = APIRouter(
	prefix = '/users',
	tags = ['User']
)



@router.get("/", response_model=List[schemas.ShowUser])
async def show_all(start: int = 0, end: int = 10, db : SessionLocal = Depends(database.get_db)):
	user = db.query(models.User).all()
	if not user:
		raise HTTPException(status_code=404, detail="No Users Found")
	return user

@router.post("/create")
async def create(request:schemas.User, db : SessionLocal = Depends(database.get_db)):

	hashed_password = hashing.get_password_hash(request.password)
	user = models.User(username=request.username, password=hashed_password)

	db.add(user)
	db.commit()
	db.refresh(user)

	return user