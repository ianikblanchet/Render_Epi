from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def get_epis(db: Session):    
    return db.query(models.EpiType).all()
    

def get_usersepis(db: Session):
    return db.query(models.Epi).join(models.EpiType).all()

def get_epi(db: Session, epi_id: int):
    return db.query(models.Epi).filter(models.Epi.id == epi_id).first()


def add_user_epi(db: Session, epi: schemas.AddEpi):
    print(epi.serial)

    if db.query(models.Epi).filter(models.Epi.serial == epi.serial).first():
    #if epi.serial == 324:
        raise HTTPException(status_code=409, detail=f'Epi with serial {epi.serial} already exists')
    else:
        new_epi = models.Epi(
                                           
                    user_id = epi.user_id,
                    epitype_id = epi.epitype_id,
                    fabricant_id = epi.fabricant_id,
                    serial = epi.serial,                   
                     
                    )
    
        db.add(new_epi)
        db.commit()
        db.refresh(new_epi)    
        return new_epi

def get_fab(db: Session):    
    return db.query(models.Fabricant).all()