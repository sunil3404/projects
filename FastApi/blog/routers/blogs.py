from fastapi import APIRouter, Depends, HTTPException
import models, schemas
from database import SessionLocal
import database
from fastapi.security import OAuth2PasswordRequestForm
import oauthtoken as oauth


router = APIRouter(
	prefix='/blog',
	tags=['Show Blogs']
)

@router.get("/")
async def show_all(db: SessionLocal = Depends(database.get_db), current_user :  OAuth2PasswordRequestForm = Depends(oauth.get_current_user)):
	blogs = db.query(models.Blog).all()
	if not blogs:
		raise HTTPException(status_code=404, detail="Blogs not found")
	return blogs

@router.get("/{id}")
async def show_by_id(id : int, db: SessionLocal = Depends(database.get_db)):
	blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
	if not blogs:
		raise HTTPException(status_code=404, detail=f"Blog with id -> {id} does not exist")
	return blogs

@router.post("/create")
async def create(request: schemas.Blogs, db: SessionLocal = Depends(database.get_db), current_user :  OAuth2PasswordRequestForm = Depends(oauth.get_current_user)):
	blog = models.Blog(title=request.title, body=request.body, user_id = db.query(models.User).filter(models.User.email == current_user.email).first().id)
	db.add(blog)
	db.commit()
	db.refresh(blog)
	return blog

@router.put("/update/{id}")
async def update(id : int, request : schemas.Blogs):
	# blog = db.query(models.Blog).filter(models.Blog.id == id).update({'title' : })
	if not blogs:
		raise HTTPException(status_code=404, detail=f"Blog with id -> {id} does not exist")
    
	return {"Message" : "Blogs updated success"}

@router.delete("/delete")
async def delete():
	return {"Message" : "Blogs delete success"}