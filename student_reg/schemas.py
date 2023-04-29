from pydantic import BaseModel
from typing import List
from models import Department

class Students_Registration(BaseModel):
    name : str
    dept_id : int
    age : int
    sex : str

    class Config:
        orm_mode = True

class Department_Reg(BaseModel):
    dept_name : str
    dept_abr  : str

    class Config:
        orm_mode = True

class Show_Student(BaseModel):
    name : str
    age : str
    mdept : Department_Reg
    class Config:
        orm_mode = True

class Show_Department(Department_Reg):
    student : List[Students_Registration] = []
     
    class Config:
        orm_mode = True

class Staff_Reg(BaseModel):

    staff_name : str
    staff_dept : str
    staff_designation : str

class Post(BaseModel):

    title : str
    content : str
    user_id :  int
    class Config:
        orm_mode = True

class User(BaseModel):

    username : str
    password : str
    email :  str
    class Config:
        orm_mode = True

class ShowPosts(BaseModel):
    title : str
    content : str
    author: User = []

    class Config:
        orm_mode =True

class ShowUser(BaseModel):
    username : str
    email : str
    post : List[Post] = []
    class Config:
        orm_mode = True
