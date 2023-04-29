from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import schemas
import models
import database
from models import Posts, User
from typing import List



router = APIRouter()


@router.post("/create_post")
def create_post(request : schemas.Post, db : Session = Depends(database.get_db)):

    userid = db.query(User).filter(User.user_id == request.user_id).first()
    
    if userid:
        new_post = Posts(title = request.title, content= request.content,
                        user_id = userid.user_id)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    else:
        raise HTTPException(status_code  = 404, detail = "user id not found")

    return new_post

@router.get("/fetch_post", response_model=List[schemas.ShowPosts])
def fetch_post(skip : int = 0, limit : int = 0 , db : Session = Depends(database.get_db)):
    posts = db.query(Posts).all()
    return posts[skip : skip + limit]


