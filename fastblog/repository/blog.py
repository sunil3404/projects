import pathlib
import sys
sys.path.append(pathlib.Path(__file__).parent.resolve())
import models, database, db_model
from fastapi import HTTPException, status


def create(request, db):
    new_blog = db_model.Blogs(title=request.title, post=request.post, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blogs(db):
    return db.query(db_model.Blogs).all()

def get_blog_by_id(id: int, db): 
    blog = db.query(db_model.Blogs).filter(db_model.Blogs.blog_id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return blog

def delete_blog(id: int, db):
    blog = db.query(db_model.Blogs).filter(db_model.Blogs.blog_id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    else:
        db.query(db_model.Blogs).filter(db_model.Blogs.blog_id == id).delete(synchronize_session=False)
        db.commit()
        return {"detail": "Blog with {id} is succesfully deleted"}
    return "Done"

def update_blog(id, request, db):
    blog = db.query(db_model.Blogs).filter(db_model.Blogs.blog_id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        db.query(db_model.Blogs).filter(db_model.Blogs.blog_id == id).\
            update({db_model.Blogs.title: request.title if request.title is not None else None,
                    db_model.Blogs.post: request.post if request.post is not None else None},
                   synchronize_session=False)
        db.commit()
    return "Updated"