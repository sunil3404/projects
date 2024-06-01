from fastapi import APIRouter, Depends, HTTPException
import schemas, models
import database
from database import SessionLocal



router = APIRouter(
	prefix = '/issue',
	tags = ['Issues']
)



@router.get("/")
async def show_all(start: int = 0, end: int = 10, db : SessionLocal = Depends(database.get_db)):
	issues = db.query(models.Issue).all()
	if not issues:
		raise HTTPException(status_code=404, detail="No Issues found")

	return issues

@router.get("/{project_name}")
async def by_project_name(project_name: str,  db : SessionLocal = Depends(database.get_db)):
	project_id = db.query(models.Project).filter(models.Project.name == project_name).first()
	if not project_id:
		raise HTTPException(status_code=404, detail=f"Project with name {project_name} -> does not exist")
	issues = db.query(models.Issue).filter(models.Issue.project_id == project_id.id).all()
	if not issues:
		raise HTTPException(status_code=404, detail="No Issues found")
	return issues

@router.post("/create")
async def create(issue : schemas.Issue, db : SessionLocal = Depends(database.get_db)):
	user_id = db.query(models.User).filter(models.User.id==issue.user_id).first().id
	project_id = db.query(models.Project).filter(models.Project.id==issue.project_id).first().id
	issue_type_id = db.query(models.IssueType).filter(models.IssueType.id==issue.issue_type_id).first().id
	proj = models.Issue(summary=issue.summary, description = issue.description, user_id = user_id, project_id=project_id, issue_type_id = issue_type_id)
	db.add(proj)
	db.commit()
	db.refresh(proj)

	return proj

@router.patch("/update/{id}")
async def update_story_points(id: int, db : SessionLocal = Depends(database.get_db)):
	issue = db.query(models.Issue).filter(models.Issue.id==id).first()
	issue.story_points=3
	db.commit()
	return issue
