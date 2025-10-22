from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int 
    name : str 
    email : str

@app.get("/users/{user_id}",response_model = User)
def get_user(user_id: int):
    return {
        "id:": user_id,
        "name": "alice",
        "email_id": "mani@gmail.com",
        "password": "mani1234"

    }