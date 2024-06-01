from fastapi import Depends, FastAPI
from routers import blogs, users, authenticate

import database
from database import SessionLocal, engine

database.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authenticate.router)