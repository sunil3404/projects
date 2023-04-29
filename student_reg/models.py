from  database import Base
from sqlalchemy import Integer, String, ForeignKey, Column, Date, TIMESTAMP
from sqlalchemy.orm import relationship
import datetime


class Department(Base):
    __tablename__ = "department"

    dept_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dept_name = Column(String, nullable=False)
    dept_abr = Column(String)
    
    student = relationship("Student", back_populates="mdept")
    staff = relationship("Staff", back_populates="department")

    def __str__(self):
        return f"{self.dept_name} --- {self.dept_abreviation}"

class Student(Base):

    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    sex = Column(String)
    date_of_joining = Column(TIMESTAMP, default=datetime.datetime.today)
    dept_id = Column(Integer, ForeignKey("department.dept_id"))

    mdept = relationship("Department", back_populates="student")

    def __str__(self):
        return f"{self.name}"


class Staff(Base):

    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    staff_name = Column(String)
    staff_designation = Column(String)
    date_of_appointment = Column(TIMESTAMP, default=datetime.datetime.today)
    dept_id = Column(Integer, ForeignKey("department.dept_id"))

    department = relationship("Department")




class User(Base):
    __tablename__ = "user"
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username  = Column(String)
    password  = Column(String)
    email = Column(String, unique=True, nullable=False)

    post = relationship("Posts", cascade="all, delete-orphan", back_populates='author')

class Posts(Base):
    __tablename__ = "posts"
    
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    author = relationship("User", passive_deletes=True, back_populates='post')

