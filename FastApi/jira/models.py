from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime


class Project(Base):

	__tablename__ = "projects"


	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)

	issues = relationship("Issue", back_populates="dept")


class IssueType(Base):

	__tablename__ = "issuetype"

	id = Column(Integer, primary_key=True, index=True)
	issue_type = Column(String)

class User(Base):
	
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)

	issues = relationship('Issue', back_populates="author")

class Issue(Base):

	__tablename__ = "issues"

	id = Column(Integer, primary_key=True, index=True)
	summary = Column(String)
	description = Column(String)
	user_id = Column(Integer, ForeignKey("users.id"))
	project_id = Column(Integer, ForeignKey("projects.id"))
	issue_type_id = Column(Integer, ForeignKey("issuetype.id"))
	story_points = Column(Integer, default = 1)
	created_datetime = Column(DateTime, default = datetime.datetime.utcnow)
	updated_datetime = Column(DateTime, default = datetime.datetime.now()) 

	author  = relationship("User", back_populates="issues")
	dept = relationship("Project", back_populates="issues")











