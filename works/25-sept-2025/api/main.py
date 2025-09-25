from fastapi import FastAPI

app = FastAPI()

@app.get("/intro")
def hello():
    return "hello checking is port changing working or not"


#to change the port use this command uvicorn main:app --reload --port 8001