from pydantic import BaseModel
from typing import List
import models


class Projects(BaseModel):
	name: str

class Issue_Type(BaseModel):
	issue_type: str

class Issue(BaseModel):
	summary: str
	description: str
	user_id: int
	project_id: int
	issue_type_id: int 
	story_points: int


class User(BaseModel):
	# id: int
	username: str
	password: str

class ShowUser(BaseModel):
	id : int
	username: str
	issues : List[Issue]

class ShowIssue(BaseModel):
	summary : str
	description: str
	story_points : int

class ShowProject(Projects):
	issues : List[ShowIssue]

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
