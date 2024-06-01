from fastapi import APIRouter, Depends
import schemas, models
import database
from database import SessionLocal



router = APIRouter(
	prefix = '/istype',
	tags = ['IssueType']
)



@router.get("/")
async def show_all(start: int = 0, end: int = 10):
	return "IssueType"

@router.post("/create")
async def create(item : schemas.Issue_Type, db : SessionLocal = Depends(database.get_db)):
	is_type = models.IssueType(issue_type=item.issue_type)

	db.add(is_type)
	db.commit()
	db.refresh(is_type)

	return is_type