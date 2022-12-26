import models
from fastapi import HTTPException, status

def add_company(request, db):
    new_comp = models.Company(name= request.name)
    db.add(new_comp)
    db.commit()
    db.refresh(new_comp)
    return new_comp

def delete_company(db, comp_name):
    comp = db.query(models.Company).filter(models.Company.name == comp_name).first()
    if not comp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{comp_name} does not exist")
    else:
        db.query(models.Company).filter(models.Company.name == comp_name).delete(synchronize_session=False)
        db.commit()
        return {"detail" : f"{comp_name} is succefully deleted"}

    
