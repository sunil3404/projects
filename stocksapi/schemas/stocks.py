from tokenize import String
import uuid
from pydantic import BaseModel
import uuid


class Stock_Details(BaseModel):
    market_cap: str

class Stocks(BaseModel):
    stock_id : uuid.uuid4()
    stocks_title: str
    stock_details: Stock_Details