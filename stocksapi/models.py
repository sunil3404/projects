from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from datetime import datetime
#from fastapi_utils.guid_type import GUID
from sqlalchemy.orm import relationship
from database import Base
import uuid
from database import engine

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Stocks_H(Base):
    __tablename__ = "stocks_h"
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable=False)
    market_cap = Column(Float)
    curr_price = Column(Float)
    high = Column(Float)
    low = Column(Float)
    stock_p_e = Column(Float)
    book_value = Column(Float)
    dividend = Column(Float)
    roce = Column(Float)
    roe = Column(Float)
    face_value = Column(Float)
    update_date = Column(DateTime, default=datetime.utcnow)

    company_id = Column(Integer, ForeignKey("company.id"))

class Stocks_D(Base):
    __tablename__ = "stocks_d"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable=False)
    market_cap = Column(Float)
    curr_price = Column(Float)
    high = Column(Float)
    low = Column(Float)
    stock_p_e = Column(Float)
    book_value = Column(Float)
    dividend = Column(Float)
    roce = Column(Float)
    roe = Column(Float)
    face_value = Column(Float)
    create_date = Column(DateTime, default=datetime.utcnow)

    company_id = Column(Integer, ForeignKey("company.id"))

