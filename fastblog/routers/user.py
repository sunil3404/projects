from fastapi import FastAPI, Depends, HTTPException, APIRouter, status, Response
from typing import List
from sqlalchemy.orm import Session
import pathlib
import sys
sys.path.append(pathlib.Path(__file__).parent.resolve())
import models, database, db_model
from hashing import Hash
from repository import user
router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post("")
def create_user(request: models.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get("/{id}", response_model=models.ShowUser)
def show_user(id : int, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)