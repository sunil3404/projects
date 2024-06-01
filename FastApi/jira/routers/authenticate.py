from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union
import schemas, models

from jose import JWTError, jwt
import database
from database import SessionLocal
import hashing
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import oauth

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



router = APIRouter(
	prefix = '/login',
	tags = ['Athenticate']
)
 

@router.post("/")
async def login(request: OAuth2PasswordRequestForm=Depends(), db:SessionLocal =Depends(database.get_db)):
	user = db.query(models.User).filter(models.User.username==request.username).first()

	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details = {"Invalid Credentials"})

	if not hashing.verify_password(request.password, user.password):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details = {"Invalid Credentials"})


	access_token = oauth.create_access_token(
        data={"sub": user.username}
    )
	return {"access_token":access_token}