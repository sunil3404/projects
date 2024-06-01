from pydantic import BaseModel
from typing import List


class Blogs(BaseModel):
	title: str
	body: str
	class Config:
		orm_mode = True


class User(BaseModel):
	email : str
	username : str
	hashed_password : str
	class Config:
		orm_mode = True


class ShowUser(BaseModel):
	id : int
	email:str
	blogs : List[Blogs]


class Login(BaseModel):
	username: str
	password : str

class ShowLoginUser(BaseModel):
	id: int
	email : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
