from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
class items(BaseModel):
    name : str 
    price: float 
    availability:Optional[bool] = None

app = FastAPI()

@app.post("/display")
def view(data:items):
    return {"message":"Item received","data":data}



#request body --> used to send the structured data to server
#pydantic model --> validation serialization documentation 
