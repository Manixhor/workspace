from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class Student(BaseModel):
    name: str 
    age: int 
    grade: str 

@app.get("/students")
def get_all_info():
    return [{"name":"Mani","age": 21,"grade": "S"}]



class Item(BaseModel):
    name: str 
    price: float 
    is_offer: bool = None 
    origin: str 

items_db = {}

@app.get("/items")
def allitems():
    return list(items_db.values())

@app.post("/items")
def adding(item:Item):
    items_db[item.name] = item 
    return item 


@app.get("/items/{name}")
def check(name:str):
    result = items_db.get(name)
    if result:
        return result
    return {"error":"Item not found"}

@app.put("/items/{name}")
def update_item(name: str, item: Item):
    items_db[name] = item
    return item