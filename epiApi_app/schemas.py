
from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel

class EpiType(BaseModel):
    id : int
    description : str
    store_num : Optional[str] 
    is_year_inpection : bool   
    #epi : List[Epi] = []

    class Config:
        orm_mode = True

class Epi(BaseModel):
    id : int     
    serial: str
    date_insp: Optional[date]
    date_year_insp : Optional[date]
    buy_date : Optional[date]
    fabricant_id : Optional[int]
    user_id : int
    epitype_id: Optional[int]
    epitype : EpiType
    
    class Config:
        orm_mode = True

class Group(BaseModel):
    id :int
    uid_manager : int
    uid_employe : int


    
class BaseUser(BaseModel):
    
    email : str
    name : str
    firstname : str
    password : str
    employe_number : Optional[str]
    level : str
    epi : Optional[List[Epi]] = []
    group_manager : Optional[List[Group]] = []
    group_employe : Optional[List[Group]] = []

    class Config:
        orm_mode = True


class User(BaseUser):
    id : Optional[int]
    
class LoginItem(BaseModel):
    email: str
    password: str

class Decode(BaseModel):
    token: str
   
class Fabricant(BaseModel):
    id : int     
    name: str
    adresse: Optional[str]
    url : Optional[str]
    
    class Config:
        orm_mode = True

class AddEpi(BaseModel):
    user_id : Optional[int] 
    epitype_id: Optional[int]
    fabricant_id : Optional[int]
    serial: Optional[str]

    class Config:
        orm_mode = True

       
        