from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    id: int

class ResponseModel(BaseModel):
    student: List[Student]
    count: int

@app.get("/coolies", response_model=ResponseModel)
def function():
    items = [Student(name="Mani", id=12)]
    return {"student": items, "count": len(items)}
