from sqlalchemy.orm import Session
import models, schemas

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.User):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
                        username = user.username,                      
                        name = user.name,
                        firstname = user.firstname,
                        employe_number = user.employe_number,
                        level = user.level,
                        email=user.email, 
                        #password_hashd=fake_hashed_password,
                        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user