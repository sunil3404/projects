from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, status
import database
import models
from sqlalchemy.orm import Session
from schemas import company
from repository import company_stocks

router = APIRouter(

    prefix="/company",
    tags=["Company"]
)


@router.post("/", response_model=company.Companies)
def company(request: company.Company, db: Session = Depends(database.get_db)):
    company = db.query(models.Company).filter(
        models.Company.name == request.name).first()
    if company:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"company {request.name} already exists in company table")
    else:
        company_stocks.add_company(request, db)
        return request

@router.delete("/{comp_name}", status_code=status.HTTP_202_ACCEPTED)
def delete_record(comp_name: str, db: Session = Depends(database.get_db)):
    return company_stocks.delete_company(db, comp_name)
