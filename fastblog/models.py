from pydantic import BaseModel
from typing import Optional,List

class Blogs(BaseModel):
    title: str
    post: Optional[str]

class BlogByUser(Blogs):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogByUser] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    post: str
    author: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

