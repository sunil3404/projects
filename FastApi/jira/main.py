from fastapi import FastAPI
from routers import projects, users, issues, issue_type, authenticate
import database
from database import SessionLocal, engine

database.Base.metadata.create_all(bind=engine)



app  = FastAPI()

app.include_router(projects.router)
app.include_router(users.router)
app.include_router(issues.router)
app.include_router(authenticate.router)
# app.include_router(issue_type.router)