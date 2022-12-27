from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from routes import epiRoute, userRoute

app = FastAPI()

app.include_router(epiRoute.router)
app.include_router(userRoute.router)



