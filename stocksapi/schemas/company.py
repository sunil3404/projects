from MySQLdb import Binary
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional


class Company(BaseModel):
    name : str

class Companies(BaseModel):
    name : str
    class Config:
        orm_mode = True