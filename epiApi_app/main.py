from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes import epiRoute, userRoute




app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
}

app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

app.include_router(epiRoute.router)
app.include_router(userRoute.router)



