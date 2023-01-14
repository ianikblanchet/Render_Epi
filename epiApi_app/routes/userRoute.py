from typing import List
import jwt
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from config import Config
from time import time
import models
import json



import cruds.userCrud as userCrud

import schemas
from database import session


router = APIRouter()

ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRES = 24000




# Dependency
def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()



@router.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = userCrud.get_users(db)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.BaseUser, db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
        #raise HTTPException(status_code=400, detail="Email already registered")
    return userCrud.create_user(db=db, user=user)

@router.post("/login")
def user_login(loginitem:schemas.LoginItem, db: Session = Depends(get_db)):

    
    data = jsonable_encoder(loginitem)
    user = userCrud.get_user(db,1)
    
    if data['email']== user.email and user.check_password(data['password']):
        print('ok3')
        encoded_jwt = jwt.encode({'email': data['email'], 'exp': time() + ACCESS_TOKEN_EXPIRES}, Config.SECRET_KEY, algorithm=ALGORITHM)
        print(encoded_jwt)
        return {"token": encoded_jwt}

    else:
        return {"message":"login failed"}


@router.get("/pass/{user_id}")
def pass_user(user_id: int, db: Session = Depends(get_db)):
    print('hello')
    db_user = userCrud.get_user(db, user_id=user_id)
    db_user.set_password('fiction')
    db.commit()
    print(db_user)
    
    
    return print('ok')


@router.post("/decode")
def token_decode(token :schemas.Decode, db: Session = Depends(get_db)):
    
    #data = json.loads(loginitem)
    print(token)
    
    
    
    if jwt.decode(token.token, Config.SECRET_KEY, algorithms=ALGORITHM)['email']:
        print('decode ok')
        
        return {"token": 'decode'}

    else:
        return {"token":"decode failed"}
