from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from hashing import Hash
import database, models, db_model
from routers import blog, user, authentication

db_model.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
