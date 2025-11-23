from fastapi import FastAPI 
from pydantic import BaseModel,Field
from typing import Optional

class imported(BaseModel):
    place: str = Field(pattern="^[a-z]")
class Items(BaseModel):
    name: str = Field(min_length =3,max_length=50,pattern="^[a-z,A-z]")
    price : float = Field(gt=0,lt=10000)
    availability: Optional[bool] = None
    manu:imported
app = FastAPI()

@app.post("/display")
def view(data:Items):
    return {"message":"Item recieved","data": data}

