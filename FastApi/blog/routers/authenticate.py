from fastapi import APIRouter, Depends, HTTPException
import models, schemas
from database import SessionLocal
import database
import hashing
import oauthtoken as token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
	prefix='/login',
	tags=['Authenticate']
)


@router.post('/')
def login(request : OAuth2PasswordRequestForm = Depends(), db : SessionLocal =Depends(database.get_db)):
	user = db.query(models.User).filter(models.User.email==request.username).first()

	if not user:
		raise HTTPException(status_code=401, detail=f"Invalid Credentials email")

	if not hashing.verify_password(request.password, user.hashed_password):
		raise HTTPException(status_code=401, detail=f"Invalid Credentials password")


	access_token = token.create_access_token(data={"sub": user.email})

	return schemas.Token(access_token=access_token, token_type="bearer")