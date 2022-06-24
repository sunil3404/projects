from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from fastapi_utils.guid_type import GUID
from sqlalchemy.orm import relationship
from database import Base
import uuid
from database import engine

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


