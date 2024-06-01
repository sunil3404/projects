from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)

	blogs = relationship("Blog", back_populates="author")


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="blogs")