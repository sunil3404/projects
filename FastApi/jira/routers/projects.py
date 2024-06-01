from fastapi import APIRouter, Depends
import schemas, models
import database
from database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
import oauth

router = APIRouter(
	prefix = '/project',
	tags = ['Projects']
)

@router.get("/", response_model=List[schemas.ShowProject])
async def show_all(db : SessionLocal = Depends(database.get_db), current_user :  OAuth2PasswordRequestForm = Depends(oauth.get_current_user)):
	projects = db.query(models.Project).all()
	if not projects:
		raise HTTPException(status_code=404, detail="No projects found")

	return projects

@router.post("/create")
async def create(project : schemas.Projects, db : SessionLocal = Depends(database.get_db)):
	proj = models.Project(name=project.name)

	db.add(proj)
	db.commit()
	db.refresh(proj)

	return proj