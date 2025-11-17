from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional


class manuf(BaseModel):
    company : str = Field(min_length=3,max_length=40,pattern="^[a-zA-z]")
    country : str
    country_code : int = Field(gt=0,lt=12)

    
class items(BaseModel):
    name : str = Field(min_length =3,max_length=50,pattern="^[a-zA-Z]")
    price: float = Field(gt=0,lt=99)
    availability:Optional[bool] = None
    #nested loop called the class manuf
    manufacturer : manuf


app = FastAPI()

@app.post("/display")
def view(data:items):
    return {"message":"Item received","data":data}



#request body --> used to send the structured data to server
#pydantic model --> validation serialization documentation 
