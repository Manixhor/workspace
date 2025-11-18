from fastapi import FastAPI 
app = FastAPI()
users = [
    {"id": 102,"dep":"CSE"},
    {"id":101,"dep":"MECH"}
]
@app.get("/users/{id}")
def read(id:int):
    return {"id is": id}

@app.get("/items/{id}")
def get_it(id:int):
    for i in users:
        if i["id"] == id:
             return i 
