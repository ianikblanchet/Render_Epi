from sqlalchemy.orm import Session
import models

def get_epis(db: Session):
    return db.query(models.Epi).all()

def get_epi(db: Session, epi_id: int):
    return db.query(models.Epi).filter(models.Epi.id == epi_id).first()

