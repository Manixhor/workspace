from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Student(BaseModel):
	name: str
	age: int
	grade : str

@app.get("/students")
def get():
	return[{"name":"mani","age": 22,"grade":"A++"},
	{"name":"ramu","age":21,"grade":"B++"}]

