from fastapi import FastAPI 

app = FastAPI()

@app.get("/hello")
def view():
    return "hello"