from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, status
import database
import models
from sqlalchemy.orm import Session
from schemas.company import Companies, Company
from repository import company_stocks

router = APIRouter(

    prefix="/company",
    tags=["Company"]
)


@router.post("/", response_model=Companies)
def company(request: Company, db: Session = Depends(database.get_db)):
    company = db.query(models.Company).filter(
        models.Company.name == request.name).first()
    if company:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"company {request.name} already exists in company table")
    else:
        company_stocks.add_company(request, db)
        return request

@router.get("/company_names")
def company_names(db: Session = Depends(database.get_db)):
    companies = db.query(models.Company).all()
    company_details = []
    for company in companies:
        company_details.append(company.name)
    return {"companies" : company_details}

@router.delete("/{comp_name}", status_code=status.HTTP_202_ACCEPTED)
def delete_record(comp_name: str, db: Session = Depends(database.get_db)):
    return company_stocks.delete_company(db, comp_name)
