from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import cruds.epiCrud as epiCrud

import schemas
from database import session


router = APIRouter()


# Dependency
def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()

#route to gather all EPI
@router.get("/epis/", response_model=List[schemas.EpiType], tags=["epis"])
def read_epis(db: Session = Depends(get_db)):
    epis = epiCrud.get_epis(db)
    print(epis[0])
    return epis

@router.get("/usersepis/", response_model=List[schemas.Epi], tags=["epis"])
def read_usersepis(db: Session = Depends(get_db)):
    usersepis = epiCrud.get_usersepis(db)    
    return usersepis

@router.post("/addusersepis/",  tags=["epis"])
def add_usersepis(epi: schemas.AddEpi, db: Session = Depends(get_db)):
    data = jsonable_encoder(epi)
    print(data["epitype_id"])
    epiCrud.add_user_epi(db=db, epi=epi)    
    return {'message':'epi ajouté'}

@router.get("/fab/", response_model=List[schemas.Fabricant], tags=["fabs"])
def read_fab(db: Session = Depends(get_db)):
    fabricant = epiCrud.get_fab(db)
    print(fabricant[0])
    return fabricant