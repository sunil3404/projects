from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session
import pathlib
import sys
sys.path.append(pathlib.Path(__file__).parent.resolve())
import models, database, db_model, oauth2
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)

@router.post("")
def create_blogs(request: models.Blogs, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get("", response_model=List[models.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.get_blogs(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=models.ShowBlog)
def show_blogs(id: int, response: Response, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.get_blog_by_id(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, response: Response, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: models.Blogs, response : Response, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)




