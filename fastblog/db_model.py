from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Blogs(Base):
    __tablename__ = "blogs"

    blog_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    post = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("Users", back_populates="blogs")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blogs", back_populates="author")