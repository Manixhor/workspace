from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional


class manf(BaseModel):
    company: str
    country: str 


class items(BaseModel):
    name : str = Field(min_length = 3,max_length =50,pattern="^[a-z,A-Z]")
    price : float = Field(gt=0,lt=10000)
    availability: Optional[bool] = None
    manufacturer : manf

app = FastAPI()
@app.post("/display/")
def view(data:items):
    return {"message":"items received","data":data}



