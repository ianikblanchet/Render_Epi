from typing import List

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
@router.get("/epis/", response_model=List[schemas.Epi], tags=["epis"])
def read_epis(db: Session = Depends(get_db)):
    epis = epiCrud.get_epis(db)
    return epis

