from jose import JWTError, jwt
import database
from database import SessionLocal
import hashing
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union
import schemas, models


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
	credentials_exception = HTTPException(
		    status_code=status.HTTP_401_UNAUTHORIZED,
		    detail="Could not validate credentials",
		    headers={"WWW-Authenticate": "Bearer"},
		)
	try:
	    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
	    username: str = payload.get("sub")
	    if username is None:
	        raise credentials_exception
	    token_data = schemas.TokenData(username=username)
	    return token_data
	except JWTError:
		raise credentials_exception