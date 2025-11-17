from fastapi import FastAPI

app = FastAPI()

#path parameter 

students = [
    {"name": "CSE","id": 101,"place": "guntur"},
     {"name": "ECE","id": 102,"place":"Hyderabad"}
]
@app.get("/display/{id}")
def view(id:str):
    for s in students:
        if s['place'] == id:
            return s 
        
#query parameter 
@app.get("/display")
def viewforquery(name:str):
    for e in students:
        if e['name'] == name:
            return e
    



