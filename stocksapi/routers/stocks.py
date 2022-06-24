from fastapi import APIRouter, Depends, HTTPException, status
from repository import beautiful_stocks as bsk
import json
import database
from sqlalchemy.orm import Session
from models import Company

with open("C:\\Users\\skumarb4\\Documents\\Projects\\webscraping\\stocksapi\\config.json", "r") as config:
    conf = json.load(config)

# companies = ["ZOMATO","3MINDIA", "RELIANCE"]

router =  APIRouter(
    
    tags=["Stocks"],
    prefix="/stocks"
)

@router.get("/")
def stocks(db :  Session = Depends(database.get_db)):
    all_stocks = []
    companies = db.query(Company).all()
    for company in companies:
        content = bsk.raw_content(conf['imp_urls']['url_screener'].format(company.name))
        stock_details = bsk.get_content(content, company.id)
        all_stocks.append(stock_details)
    return {"stock_details" : all_stocks}

@router.get("/{stock_name}")
def stocks(stock_name : str, db: Session = Depends(database.get_db)):
    comp = db.query(Company).filter(Company.name == stock_name).first()
    if not comp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_name} not found")
    content = bsk.raw_content(conf['imp_urls']['url_screener'].format(comp.name))
    return bsk.get_content(content, comp.id)

    