
from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel


class Epi(BaseModel):
    id : int     
    serial: str
    date_insp: Optional[date]
    date_year_insp : Optional[date]
    buy_date : Optional[date]
    user_id : int
    epitype_id: Optional[int]

    class Config:
        orm_mode = True

class Group(BaseModel):
    id :int
    uid_manager : int
    uid_employe : int

class EpiType(BaseModel):
    id : int
    description : str
    store_num : str  
    url_fabricant : str
    is_year_inpection : bool
    epi : List[Epi] = []

    class Config:
        orm_mode = True
    
class BaseUser(BaseModel):
    username : str
    email : str
    name : str
    firstname : str
    employe_number : Optional[str]
    level : str
    epi : Optional[List[Epi]] = []
    group_manager : Optional[List[Group]] = []
    group_employe : Optional[List[Group]] = []

    class Config:
        orm_mode = True


class User(BaseUser):
    id : int
    


